import unittest
from ..lib.ex0008 import *


#class MyTestCase(unittest.TestCase):
class MyTestCase(object):
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


perr(f1(
    [["a"], [[["a"]]]]
))
