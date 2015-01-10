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

    def Out(self, data):
        pass


class Out(State):
    pass


sm1 = StateMachine([In, A, B, Out])


class In1(State):
    def A1(self, data):
        pass


class A1(State):
    def A1(self, data):
        pass

    def B(self, data):
        self.state_machine.result = data
    B.state = 'B1'


class B1(State):
    def B(self, data):
        pass
    B.state = 'B1'

    def Out(self, data):
        pass


sm2 = StateMachine([In1, A1, B1, Out])


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

    def test_0002(self):
        sm2.run([
            {'name': 'A1', 'data': 'data of A1'},
            {'name': 'A1', 'data': 'data of A2'},
            {'name': 'B', 'data': 'data of B'},
        ])
        self.assertEqual(
            sm1.result,
            'data of B'
        )
