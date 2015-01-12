import unittest
from ..lib.ex0006 import Node, SeqNode, Char, Seq, Or, Star, MayBe, InputChar, AutomatonException


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
        with self.assertRaises(AutomatonException):
            o = g.run(x)

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
        with self.assertRaises(AutomatonException):
            o = g.run(x)

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

    def test_Or(self):
        g = Or(Char('a'), Char('b'), name='Or 1')
        x = iter([
            InputChar('a'),
        ])
        o = g.run(x)
        print(o)
        y = InputChar('a')
        self.assertEqual(
            o,
            y
        )

    def test_Or2(self):
        g = Or(Char('a'), Char('b'), name='Or 1')
        x = iter([
            InputChar('b'),
        ])
        o = g.run(x)
        print(o)
        y = InputChar('b')
        self.assertEqual(
            o,
            y
        )

    def test_Seq_Or(self):
        g = Or(
            Seq(
                Char('a'),
                name='branch a'
            ),
            Char('b')
        )
        x = iter([
            InputChar('a'),
        ])
        y = SeqNode([InputChar('a')])
        self.assertEqual(
            g.run(x),
            y
        )

    def test_Star(self):
        g = Seq(
            Char('a'),
            Star(
                Char('b')
            ),
        )
        x = iter([
            InputChar('a'),
            InputChar('b'),
            InputChar('b'),
            InputChar('b'),
        ])
        o = g.run(x)
        print(o)
        y = SeqNode([
            InputChar('a'),
            SeqNode([
                InputChar('b'),
                InputChar('b'),
                InputChar('b'),
            ])
        ])
        self.assertEqual(
            o,
            y
        )

    def test_exception(self):
        g = Seq(
            Char('a'),
            Char('b')
        )
        x = iter([
            InputChar('a'),
            InputChar('b'),
            InputChar('c'),
            InputChar('d'),
        ])
        with self.assertRaises(AutomatonException):
            o = g.run(x)

    def test_MayBe(self):
        g = Seq(
            Char('a'),
            MayBe(Char('b'))
        )
        x = iter([
            InputChar('a'),
            InputChar('b'),
        ])
        o = g.run(x)
        print(o)
        y = SeqNode([
            InputChar('a'),
            SeqNode([
                InputChar('b'),
            ])
        ])
        self.assertEqual(
            o,
            y
        )

    def test_MayBe_doesn_t_consume_all(self):
        g = Seq(
            Char('a'),
            MayBe(Char('b'))
        )
        x = iter([
            InputChar('a'),
            InputChar('b'),
            InputChar('b'),
        ])
        with self.assertRaises(AutomatonException):
            o = g.run(x)
