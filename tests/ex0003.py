#coding: UTF-8
from __future__ import unicode_literals
import unittest
from collections import OrderedDict

from ..lib.ex0003 import parse_articles, LineKind

class LineKindTestCase(unittest.TestCase):
    def test_empty_line_is_NOTHING(self):
        self.assertEqual(
            LineKind.for_line(''),
            LineKind.NOTHING
        )

    def test_ENDING(self):
        self.assertEqual(
            LineKind.for_line('\t'),
            LineKind.ENDING
        )

    def test_when_starting_not_from_tab__something_meaningful_is_NAME(self):
        self.assertEqual(
            LineKind.for_line('статья'),
            LineKind.NAME
        )

    def test_when_starting_not_from_tab__something_meaningless_is_NOTHING(self):
        self.assertEqual(
            LineKind.for_line(' ' * 3),
            LineKind.NOTHING
        )

    def test_when_starting_from_tab__empty_line_is_NOTHING(self):
        self.assertEqual(
            LineKind.for_line('\t   '),
            LineKind.NOTHING
        )

    def test_when_starting_from_tab__non_empty_line_is_BODY(self):
        self.assertEqual(
            LineKind.for_line('\tслово'),
            LineKind.BODY
        )


one_article = '''\
ы
\tи
\t'''

class ParseArticlesTestCase(unittest.TestCase):
    def test_0001(self):
        self.assertEqual(
            parse_articles(''),
            OrderedDict([])
        )

    def t1est_0002(self):
        self.assertEqual(
            parse_articles(one_article),
            OrderedDict([('ы', ['и'])]),
        )
