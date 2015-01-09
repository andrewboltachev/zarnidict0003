import unittest
from ..lib.ex0002 import f


class SimpleRDTestCase(unittest.TestCase):
    def test_0001(self):
        self.assertEqual(
            f(['[pre]', '[/pre]']),
            [{'name': 'pre', 'data': []}]
        )

    def test_0002(self):
        self.assertEqual(
            f(['[pre]', 'foo', '[/pre]']),
            [{'name': 'pre', 'data': ['foo']}]
        )

    def test_0003(self):
        self.assertEqual(
            f(['[pre]', 'foo', 'bar', 'buz', '[/pre]']),
            [{'name': 'pre', 'data': ['foo', 'bar', 'buz']}]
        )

    def test_0004(self):
        self.assertEqual(
            f(['[pre]', 'foo', 'bar', '[/pre]', 'buz']),
            [{'name': 'pre', 'data': ['foo', 'bar']}, 'buz']
        )

class NestedRDTestCase(unittest.TestCase):
    def test_0001(self):
        self.assertEqual(
            f(['[pre]', 'foo', 'bar', '[/pre]', 'buz']),
            [{'name': 'pre', 'data': ['foo', 'bar']}, 'buz']
        )
