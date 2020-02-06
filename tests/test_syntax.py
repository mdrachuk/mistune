import mistune2
from tests import BaseTestCase


class TestSyntax(BaseTestCase):
    def assert_case(self, n, text, html):
        result = mistune2.html(text)
        self.assertEqual(result, html)


TestSyntax.load_fixtures('syntax.md')
TestSyntax.load_fixtures('non-commonmark.txt')
