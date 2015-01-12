import unittest
from ..lib.ex0006 import Node, SeqNode, Char, Seq, Or, Star, InputChar


class MyTestCase(unittest.TestCase):
    maxDiff = None

    def tes1t_0001(self):
        g = Or(
            Seq(
                Char('a'),
                name='branch a'
            ),
            Star(
                Char('b'),
                name='branch b'
            )
        )
        x = iter([
            Char('a'),
        ])
        y = Node(Node(['a']))
        self.assertEqual(
            g.process(x),
            y
        )

    def test_Char(self):
        g = Char('a')
        x = iter([
            InputChar('a'),
        ])
        o = g.process(x)
        y = Node(InputChar('a'))
        self.assertEqual(
            o,
            y
        )

    def test_Char_neg(self):
        g = Char('b')
        x = iter([
            InputChar('a'),
        ])
        o = g.process(x)
        self.assertEqual(
            o,
            None
        )

    def test_Seq_single(self):
        g = Seq(Char('a'))
        x = iter([
            InputChar('a'),
        ])
        o = g.process(x)
        print(o)
        y = SeqNode([Node(InputChar('a'))])
        self.assertEqual(
            o,
            y
        )

    def test_Seq(self):
        g = Seq(Char('a'), Char('b'))
        x = iter([
            InputChar('a'),
            InputChar('b'),
        ])
        o = g.process(x)
        print(o)
        y = SeqNode([Node(InputChar('a')), Node(InputChar('b'))])
        self.assertEqual(
            o,
            y
        )
    '''
    '''
