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
            g.run(x),
            y
        )

    def test_Char(self):
        g = Char('a')
        x = iter([
            InputChar('a'),
        ])
        o = g.run(x)
        y = InputChar('a')
        self.assertEqual(
            o,
            y
        )

    def test_Char_neg(self):
        g = Char('b')
        x = iter([
            InputChar('a'),
        ])
        o = g.run(x)
        self.assertEqual(
            o,
            None
        )

    def test_Seq_single(self):
        g = Seq(Char('a'))
        x = iter([
            InputChar('a'),
        ])
        o = g.run(x)
        print(o)
        y = SeqNode([InputChar('a')])
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
        o = g.run(x)
        print(o)
        y = SeqNode([InputChar('a'), InputChar('b')])
        self.assertEqual(
            o,
            y
        )

    def test_Seq_neg(self):
        g = Seq(Char('a'), Char('b'))
        x = iter([
            InputChar('a'),
            InputChar('a'),
        ])
        o = g.run(x)
        print(o)
        y = SeqNode([InputChar('a'), InputChar('b')])
        self.assertEqual(
            o,
            None
        )

    def test_Seq_to_json_like(self):
        g = Seq(Char('a'), Char('b'), name='name 1')
        x = iter([
            InputChar('a', 'payload a'),
            InputChar('b', 'this is payload b'),
        ])
        o = g.run(x).to_json_like()
        print(o)
        y = {
            'name': 'name 1',
            'klass': 'Seq',
            'content': [
                {
                    'name': 'a',
                    'payload': 'payload a',
                },
                {
                    'name': 'b',
                    'payload': 'this is payload b',
                },
            ]
        }
        self.assertEqual(
            o,
            y
        )

