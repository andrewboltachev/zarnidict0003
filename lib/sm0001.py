from lib.ex0004 import State, StateMachine, to_state, state_pfx


class In(State):
    def pre(self, data):
        pass

    def trn(self, data):
        pass

    def m1(self, data):
        pass


class pre(State):
    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def G(self, data):
        pass

    def end(self, data):
        pass

    def R(self, data):
        pass

    def GG(self, data):
        pass


class end(State):
    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def GG(self, data):
        pass


class G(State):
    def gor(self, data):
        pass


class gor(State):
    def trn(self, data):
        pass

    def end(self, data):
        pass

    def m1(self, data):
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
    @state_pfx('R_')
    def trn(self, data):
        pass

    @state_pfx('R_')
    def m1(self, data):
        pass

    @state_pfx('R_')
    def G(self, data):
        pass

    @state_pfx('R_')
    def end(self, data):
        pass


class R_G(State):
    @state_pfx('R_')
    def gor(self, data):
        pass


class R_end(State):
    @state_pfx('R_')
    def trn(self, data):
        pass

    @state_pfx('R_')
    def m1(self, data):
        pass


class R_gor(State):
    @state_pfx('R_')
    def trn(self, data):
        pass

    @state_pfx('R_')
    def end(self, data):
        pass

    @state_pfx('R_')
    def m1(self, data):
        pass


class R_m1(State):
    @state_pfx('R_')
    def trn(self, data):
        pass


class R_trn(State):
    @state_pfx('R_')
    def trn(self, data):
        pass

    @state_pfx('R_')
    def mhr(self, data):
        pass

    @state_pfx('R_')
    def ex(self, data):
        pass

    @state_pfx('R_')
    def exi(self, data):
        pass

    def Out(self, data):
        pass


class R_mhr(State):
    @state_pfx('R_')
    def u(self, data):
        pass

    @state_pfx('R_')
    def rus(self, data):
        pass


class R_u(State):
    @state_pfx('R_')
    def rus(self, data):
        pass


class R_rus(State):
    @state_pfx('R_')
    def mhr(self, data):
        pass

    @state_pfx('R_')
    def trn(self, data):
        pass

    @state_pfx('R_')
    def ex(self, data):
        pass

    @state_pfx('R_')
    def exi(self, data):
        pass

    def R(self, data):
        pass

    def Out(self, data):
        pass


class R_ex(State):
    @state_pfx('R_')
    def ref(self, data):
        pass


class R_ref(State):
    @state_pfx('R_')
    @to_state('ref_COMMA')
    def COMMA(self, data):
        pass

    @state_pfx('R_')
    def exi(self, data):
        pass

    @state_pfx('R_')
    def trn(self, data):
        pass

    def Out(self, data):
        pass


class R_ref_COMMA(State):
    @state_pfx('R_')
    def ref(self, data):
        pass


class R_exi(State):
    @state_pfx('R_')
    def m1dash(self, data):
        pass


class R_m1dash(State):
    @state_pfx('R_')
    def m1dash(self, data):
        pass

    def R(self, data):
        pass

    def Out(self, data):
        pass


class GG(State):
    @state_pfx('G_')
    def trn(self, data):
        pass


class G_trn(State):
    @state_pfx('G_')
    def mrj(self, data):
        pass


class G_mrj(State):
    @state_pfx('G_')
    def rus(self, data):
        pass

    @state_pfx('G_')
    def u(self, data):
        pass


class G_u(State):
    @state_pfx('G_')
    def rus(self, data):
        pass


class G_rus(State):
    @state_pfx('G_')
    def trn(self, data):
        pass

    def Out(self, data):
        pass


sm = StateMachine([
    In,
    pre, G, end, gor, m1, trn, mhr, u, rus, ex, ref, ref_COMMA, exi, m1dash,
    R,
    R_G, R_G, R_end, R_gor, R_m1, R_trn, R_mhr, R_u, R_rus, R_ex, R_ref, R_ref_COMMA, R_exi, R_m1dash,
    GG, G_trn, G_mrj, G_u, G_rus,
    Out])
