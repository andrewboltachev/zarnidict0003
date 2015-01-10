from lib.ex0004 import State, StateMachine, to_state


class In(State):
    def pre(self, data):
        pass

    def trn(self, data):
        pass


class pre(State):
    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def G(self, data):
        pass

    def R(self, data):
        pass

    def end(self, data):
        pass


class end(State):
    def trn(self, data):
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

    def ex(self, data):
        pass

    def exi(self, data):
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

    def exi(self, data):
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

    def exi(self, data):
        pass

    def trn(self, data):
        pass

    def Out(self, data):
        pass


class ref_COMMA(State):
    def ref(self, data):
        pass


class exi(State):
    def m1dash(self, data):
        pass


class m1dash(State):
    def m1dash(self, data):
        pass

    def Out(self, data):
        pass


class Out(State):
    pass


class R(State):
    @to_state('R_G')
    def g(self, state):
        pass


class R_G(State):
    @to_state('R_gor')
    def gor(self, data):
        pass


class R_gor(State):
    @to_state('R_trn')
    def trn(self, data):
        pass


class R_trn(State):
    @to_state('R_trn')
    def trn(self, data):
        pass

    @to_state('R_mhr')
    def mhr(self, data):
        pass

    @to_state('R_ex')
    def ex(self, data):
        pass

    @to_state('R_exi')
    def exi(self, data):
        pass

    def Out(self, data):
        pass


class R_mhr(State):
    def u(self, data):
        pass

    def rus(self, data):
        pass


class R_u(State):
    def rus(self, data):
        pass


class R_rus(State):
    def mhr(self, data):
        pass

    def trn(self, data):
        pass

    def ex(self, data):
        pass

    def exi(self, data):
        pass

    def Out(self, data):
        pass


class R_ex(State):
    def ref(self, data):
        pass


class R_ref(State):
    @to_state('ref_COMMA')
    def COMMA(self, data):
        pass

    def exi(self, data):
        pass

    def trn(self, data):
        pass

    def Out(self, data):
        pass


class R_ref_COMMA(State):
    def ref(self, data):
        pass


class R_exi(State):
    def m1dash(self, data):
        pass


class R_m1dash(State):
    def m1dash(self, data):
        pass

    def Out(self, data):
        pass


sm = StateMachine([
    In,
    pre, G, end, gor, m1, trn, mhr, u, rus, ex, ref, ref_COMMA, exi, m1dash,
    R,
    R_G, R_gor, R_trn,
    Out])
