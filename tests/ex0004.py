import unittest
from ..lib.ex0004 import State, StateMachine

class In(State):
    def A(self, data):
        pass


class A(State):
    def A(self, data):
        pass

    def B(self, data):
        self.state_machine.result = data


class B(State):
    def B(self, data):
        pass

    def eoi(self, data):
        pass


sm1 = StateMachine([In, A, B])


class SimpleSMTestCase(unittest.TestCase):
    def test_0001(self):
        sm1.run([
            {'name': 'A', 'data': 'data of A1'},
            {'name': 'A', 'data': 'data of A2'},
            {'name': 'B', 'data': 'data of B'},
        ])
        self.assertEqual(
            sm1.result,
            'data of B'
        )
