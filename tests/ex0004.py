import unittest
from ..lib.ex0004 import State, StateMachine, to_state, state_pfx

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
    @to_state('A1')
    def A(self, data):
        pass


class A1(State):
    def A(self, data):
        pass
    A.state = 'A1'

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


class In2(State):
    @state_pfx('X')
    def A2(self, data):
        pass


class XA2(State):
    @state_pfx('X')
    def A2(self, data):
        pass

    def B2(self, data):
        self.state_machine.result = data


class B2(State):
    def B2(self, data):
        pass

    def Out(self, data):
        pass


sm3 = StateMachine([In2, XA2, B2, Out])


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
            {'name': 'A', 'data': 'data of A1'},
            {'name': 'A', 'data': 'data of A2'},
            {'name': 'B', 'data': 'data of B'},
        ])
        self.assertEqual(
            sm1.result,
            'data of B'
        )

    def test_0003(self):
        sm3.run([
            {'name': 'A2', 'data': 'data of A1'},
            {'name': 'A2', 'data': 'data of A2'},
            {'name': 'B2', 'data': 'data of B'},
        ])
        self.assertEqual(
            sm1.result,
            'data of B'
        )
