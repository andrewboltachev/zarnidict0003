import unittest
from ..lib.ex0008 import *
import sys

def perr(x):
    sys.stderr.write(str(x) + '\n')


class MyTestCase(unittest.TestCase):
    def te1st_int(self):
        self.assertEqual(
            f1(
                [[1], [[1]]]
                ),
                []
            )

    def test_deg_0001(self):
        self.assertEqual(
            f1(
                []
                ),
            {0: []}
            )

    def test_deg_0002(self):
        self.assertEqual(
            f1(
                [[]]
                ),
            {0: [{'link': 1}],
             1: []}
            )


perr(mark_depth(
                [[1], [[[1]]]]
    ))
