import unittest
from ..lib.ex0006 import Node, SeqNode, Char, Seq, Or, Star, MayBe, InputChar, AutomatonException, Automaton, tail_length


class ToEdnLikeTestCase(unittest.TestCase):
    def test_Char(self):
        g = Char('a', 1)
        self.assertEqual(g.to_edn_like(),
            {'type': 'Char', 'value': 'a', 'payload': 1}
        )
    def test_Char_no_payload(self):
        g = Char('a')
        self.assertEqual(g.to_edn_like(),
            {'type': 'Char', 'value': 'a', 'payload': None}
        )

    def test_Seq(self):
        a = Char('a', 'c1')
        b = Char('b', 'c2')
        c = Char('c', 'c3')

        a_e = a.to_edn_like()
        b_e = b.to_edn_like()
        c_e = c.to_edn_like()

        g = Seq(*[a, b, c], name='s1')
        print(g.args)
        self.assertEqual(
                {'type': 'Seq', 'value': [a_e, b_e, c_e], 'payload': 's1'},
g.to_edn_like()
        )


