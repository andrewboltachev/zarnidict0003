import unittest
from collections import OrderedDict
from ..lib.ex0005 import Or, Plus, Star, get_first_terminal, Expr as e


class SyntaxTestCase(unittest.TestCase):
    def test_0001(self):
        EX = e('EX', Or(['mhr', 'u', 'rus'], ['mhr', 'rus']))
        B_a = e('B_a', 'trn', Star([EX]))
        '''
        OrderedDict([
            ('A', [Or(['L_a', 'R_a', 'B_a'])]),
            ('L_a', [Plus(['L_el'])]),
            ('L_el', ['L', Or(['R_a', 'B_a'])]),
            ('R_a', [Plus(['R_el'])]),
            ('R_el', ['R', 'B_a']),
            ('B_a', ['trn', Star(['EX'])]),
            ('EX', [Or([['mhr', 'u', 'rus'], ['mhr', 'rus']])]),
        ])
        '''


class GetFirstTerminalTestCase(unittest.TestCase):
    def test_single_terminal(self):
        A = e('A', 'a')

        self.assertEqual(
            get_first_terminal(A),
            {'A': ['a']}
        )

    def test_two_terminals(self):
        A = e('A', 'a', 'b')

        self.assertEqual(
            get_first_terminal(A),
            {'A': ['a', 'b']}
        )

    def test_one_terminal_nested(self):
        A = e('A', ['a'])

        self.assertEqual(
            get_first_terminal(A),
            {'A': {'': ['a']}}
        )

    '''
    def test_single_level_of_(self):
        g = OrderedDict([
            ('A', 'B'),
            ('B', 'b'),
        ])

        self.assertEqual(
            get_first_terminal(g),
            ['b']
        )
    '''
