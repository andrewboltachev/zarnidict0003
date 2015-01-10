from lib.ex0004 import State, StateMachine, to_state


class In(State):
    def pre(self, data):
        pass


class pre(State):
    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def G(self, data):
        pass


class G(State):
    def gor(self, data):
        pass


class gor(State):
    def trn(self, data):
        pass


class m1(State):
    def trn(self, data):
        pass


class trn(State):
    def trn(self, data):
        pass

    def mhr(self, data):
        pass

    def Out(self, data):
        pass


class mhr(State):
    def u(self, data):
        pass

    def rus(self, data):
        pass


class u(State):
    def rus(self, data):
        pass


class rus(State):
    def mhr(self, data):
        pass

    def trn(self, data):
        pass

    def ex(self, data):
        pass

    def Out(self, data):
        pass


class ex(State):
    def ref(self, data):
        pass


class ref(State):
    @to_state('ref_COMMA')
    def COMMA(self, data):
        pass

    def Out(self, data):
        pass


class ref_COMMA(State):
    def ref(self, data):
        pass


class Out(State):
    pass


sm = StateMachine([In, pre, G, gor, m1, trn, mhr, u, rus, ex, ref, ref_COMMA, Out])
