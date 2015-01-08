import unittest
from ..lib.ex0001 import simple_bnf, SimpleBNFError


class SimpleBNFTestCase(unittest.TestCase):
    def assertResult(self, grammar, data, result):
        self.assertEqual(
            simple_bnf(grammar, data),
            result
        )

    def assertResultEqualToGrammar(self, grammar, data):
        self.assertResult(grammar, data, grammar)

    def assertResultIsBad(self, grammar, data):
        with self.assertRaises(SimpleBNFError):
            simple_bnf(grammar, data)

    
    def test_0001(self):
        self.assertResultEqualToGrammar(
            {'name': 'root', 'data': '.'},
            '.'
        )
        self.assertResultEqualToGrammar(
            {'name': 'root', 'data': ','},
            ','
        )

    def test_0002(self):
        self.assertResultIsBad(
            {'name': 'root', 'data': ','},
            '.'
        )

    # 2-level case
    def test_0003(self):
        self.assertResultEqualToGrammar(
            {'name': 'root', 'data':
                {'name': 'foo', 'data': ','}
            },
            ','
        )

    def test_0004(self):
        self.assertResultIsBad(
            {'name': 'root', 'data':
                {'name': 'foo', 'data': ','}
            },
            '.'
        )

    # 3-level case
    def test_0005(self):
        self.assertResultEqualToGrammar(
            {'name': 'root', 'data':
                {'name': 'foo', 'data':
                    {'name': 'bar', 'data': ','}
                }
            },
            ','
        )

    # sequences
    def test_0006(self):
        self.assertResultEqualToGrammar(
            {'name': 'root', 'data':
                {'name': 'foo', 'data':
                    [
                        {'name': 'bar', 'data': '.'},
                        {'name': 'buz', 'data': ','}
                    ]
                }
            },
            '.,'
        )

