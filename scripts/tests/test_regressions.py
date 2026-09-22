#!/usr/bin/env python3
"""Offline regressions for marker completeness and citation verdict correctness."""

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1]


def load_script(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load_script('citation-verify.py')
consistency = load_script('citation-consistency.py')


class PendingMarkerTests(unittest.TestCase):
    def scan(self, text, directory=False):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            draft = root / 'draft with spaces.md'
            draft.write_text(text, encoding='utf-8')
            (root / 'ignored.txt').write_text('[VERIFY]\n', encoding='utf-8')
            return subprocess.run(
                ['bash', str(SCRIPTS / 'pending-checks.sh'), str(root if directory else draft)],
                capture_output=True, text=True, check=True,
            ).stdout

    def test_all_english_markers_are_reported(self):
        markers = ['[VERIFY]', '❓ to discuss', '[AI DRAFT]', '>>>', '[author micro-adjustment]']
        output = self.scan('\n'.join(markers))
        self.assertIn('5 pending item(s) total', output)
        for line, marker in enumerate(markers, 1):
            self.assertIn(f'{line}:{marker}', output)

    def test_mixed_language_directory_and_markdown_filter(self):
        output = self.scan('[VERIFY]\n[待核对]\n[AI 草稿]\n[AI DRAFT]\n', directory=True)
        self.assertIn('4 pending item(s) total', output)
        self.assertIn('draft with spaces.md:1:[VERIFY]', output)
        self.assertNotIn('ignored.txt', output)

    def test_documented_verbose_draft_marker(self):
        output = self.scan('[AI draft, pending author review]\n[AI 草稿，待作者审阅]\n')
        self.assertIn('2 pending item(s) total', output)

    def test_unmarked_prose_does_not_match(self):
        output = self.scan('VERIFY the source. [VERIFIED] [AI DRAFTED]\n')
        self.assertIn('0 pending item(s) total', output)


class CitationVerdictTests(unittest.TestCase):
    def setUp(self):
        sleeper = patch.object(verify.time, 'sleep', lambda _: None)
        sleeper.start()
        self.addCleanup(sleeper.stop)

    def candidate(self, surname):
        return {'author': [{'family': surname}], 'title': ['Another Paper']}

    def check_candidate(self, surname):
        with patch.object(verify, 'crossref_query', return_value=[self.candidate(surname)]), \
                patch.object(verify, 'openalex_query', return_value=[]):
            return verify.verify('(Smith, 2010)')

    def test_near_surname_requires_review(self):
        result = self.check_candidate('Smiths')  # similarity 0.91, formerly FOUND
        self.assertEqual('FUZZY_MATCH', result[0]['verdict'])
        self.assertEqual(1, verify.exit_code(result))
        self.assertEqual('Another Paper', result[0]['match']['title'])

    def test_exact_surname_ignores_case_and_outer_space(self):
        result = self.check_candidate(' SMITH ')
        self.assertEqual('FOUND', result[0]['verdict'])
        self.assertEqual(0, verify.exit_code(result))

    def check_responses(self, crossref, openalex):
        def fetch(url):
            return crossref if url.startswith(verify.CROSSREF_URL) else openalex
        with patch.object(verify, '_fetch_json', side_effect=fetch):
            result = verify.verify('(Smith, 2010)')
        self.assertEqual('ERROR', result[0]['verdict'])
        self.assertEqual(2, verify.exit_code(result))
        self.assertTrue(result[0]['errors'])

    def test_malformed_crossref_is_error_not_absence(self):
        for response in [
            {'error': 'temporarily unavailable'}, [], {'message': None},
            {'message': {'items': None}}, {'message': {'items': [None]}},
            {'message': {'items': [{'author': 'Smith'}]}},
            {'message': {'items': [{'title': 'A plain string is not a title list'}]}},
        ]:
            with self.subTest(response=response):
                self.check_responses(response, {'results': []})

    def test_malformed_openalex_is_error_without_traceback(self):
        for response in [
            {'results': None}, [], {'results': [None]},
            {'results': [{'authorships': None}]},
            {'results': [{'authorships': [{'author': {'display_name': 123}}]}]},
            {'results': [{'display_name': ['Not a string']}]},
        ]:
            with self.subTest(response=response):
                self.check_responses({'message': {'items': []}}, response)

    def test_valid_empty_responses_remain_not_found(self):
        with patch.object(verify, '_fetch_json', side_effect=[
            {'message': {'items': []}}, {'results': []},
        ]):
            result = verify.verify('(Smith, 2010)')
        self.assertEqual('NOT_FOUND', result[0]['verdict'])

    def test_backend_failure_can_recover_with_other_backend(self):
        with patch.object(verify, '_fetch_json', side_effect=[
            {'error': 'temporarily unavailable'},
            {'results': [{'authorships': [{'author': {'display_name': 'Jane Smith'}}],
                          'display_name': 'Recovered Paper'}]},
        ]):
            result = verify.verify('(Smith, 2010)')
        self.assertEqual('FOUND', result[0]['verdict'])
        self.assertEqual('OpenAlex', result[0]['source'])
        self.assertTrue(result[0]['errors'])

    def test_empty_optional_title_list_does_not_crash(self):
        with patch.object(verify, '_fetch_json', return_value={
            'message': {'items': [{'author': [{'family': 'Smith'}], 'title': []}]},
        }):
            result = verify.verify('(Smith, 2010)')
        self.assertEqual('', result[0]['match']['title'])


class PageConsistencyTests(unittest.TestCase):
    def page_warnings(self, text):
        return [line for line in consistency.scan(text) if 'Inconsistent page-number formats' in line]

    def test_singular_and_plural_pages_are_one_style(self):
        self.assertEqual([], self.page_warnings('(Smith, 2010, p. 2) and (Jones, 2011, pp. 3–4).'))

    def test_chinese_page_and_range_are_one_style(self):
        self.assertEqual([], self.page_warnings('第 2 页和第 3–4 页。'))

    def test_spacing_difference_is_still_reported(self):
        self.assertTrue(self.page_warnings('p. 2 and pp.3–4'))

    def test_english_chinese_page_styles_still_reported(self):
        self.assertTrue(self.page_warnings('pp. 3–4 和第 5 页'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
