from lib.ex0004 import State, StateMachine, to_state, state_pfx


class In(State):
    def pre(self, data):
        pass

    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def GG(self, data):
        pass

    def end(self, data):
        pass

    def L(self, data):
        pass

    def G(self, data):
        pass

    def R(self, data):
        pass

    def ex(self, data):
        pass


class L(State):
    def R(self, data):
        pass
    
    def pre(self, data):
        pass


class pre(State):
    def ex(self, data):
        pass

    def mhr(self, data):
        pass

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

    def L(self, data):
        pass
    
    def GG(self, data):
        pass

    def exi(self, data):
        pass

    def Out(self, data):
        pass


class end(State):
    def end(self, data):
        pass

    def mhr(self, data):
        pass

    def ex(self, data):
        pass

    def G(self, data):
        pass

    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def GG(self, data):
        pass

    def exi(self, data):
        pass


class G(State):
    def gor(self, data):
        pass


class gor(State):
    def exi(self, data):
        pass

    def R(self, data):
        pass

    def trn(self, data):
        pass

    def end(self, data):
        pass

    def m1(self, data):
        pass


class m1(State):
    def end(self, data):
        pass

    def ex(self, data):
        pass

    def mrj(self, data):
        pass

    def trn(self, data):
        pass

    def R(self, data):
        pass

    def G(self, data):
        pass

    def mhr(self, data):
        pass

    def exi(self, data):
        pass

    def Out(self, data):
        pass


class trn(State):
    def GG(self, data):
        pass

    def m1dash(self, data):
        pass

    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def mhr(self, data):
        pass

    def mrj(self, data):
        pass

    def ex(self, data):
        pass

    def exi(self, data):
        pass

    def R(self, data):
        pass

    def L(self, data):
        pass
    
    def Out(self, data):
        pass


class mhr(State):
    def u(self, data):
        pass

    def rus(self, data):
        pass


class mrj(State):
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

    def mrj(self, data):
        pass

    def trn(self, data):
        pass

    def ex(self, data):
        pass

    def exi(self, data):
        pass

    def R(self, data):
        pass

    def L(self, data):
        pass
    
    def Out(self, data):
        pass


class ex(State):
    def ref(self, data):
        pass

    def add(self, data):
        pass

    def m1(self, data):
        pass


class ref(State):
    def pre(self, data):
        pass

    def mhr(self, data):
        pass

    @to_state('ref_COMMA')
    def COMMA(self, data):
        pass

    def m1dash(self, data):
        pass

    def ref(self, data):
        pass

    def exi(self, data):
        pass

    def trn(self, data):
        pass

    def ex(self, data):
        pass

    def add(self, data):
        pass

    def Out(self, data):
        pass

    def R(self, data):
        pass

    def L(self, data):
        pass
    

class add(State):
    def m1(self, data):
        pass

    @to_state('ref_COMMA')
    def COMMA(self, data):
        pass

    def exi(self, data):
        pass

    def trn(self, data):
        pass

    def ref(self, data):
        pass

    def ex(self, data):
        pass

    def R(self, data):
        pass

    def Out(self, data):
        pass


class ref_COMMA(State):
    def ref(self, data):
        pass


class exi(State):
    def mhr(self, data):
        pass

    def m1dash(self, data):
        pass


class m1dash(State):
    def trn(self, data):
        pass

    def mhr(self, data):
        pass

    def m1dash(self, data):
        pass

    def R(self, data):
        pass

    def L(self, data):
        pass
    
    def exi(self, data):
        pass

    def Out(self, data):
        pass


class Out(State):
    pass


class R(State):
    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def G(self, data):
        pass

    def end(self, data):
        pass

    def exi(self, data):
        pass

    def GG(self, data):
        pass

    def pre(self, data):
        pass


class GG(State):
    def ex(self, data):
        pass

    def pre(self, data):
        pass

    def trn(self, data):
        pass

    def m1(self, data):
        pass

    def GG(self, data):
        pass

    def end(self, data):
        pass

    def exi(self, data):
        pass

    def R(self, data):
        pass

    def mrj(self, data):
        pass


sm = StateMachine([
    In,
    pre, G, end, gor, m1, trn, mhr, mrj, u, rus, ex, ref, add, ref_COMMA, exi, m1dash,
    L,
    R,
    #R_G, R_G, R_end, R_gor, R_m1, R_trn, R_mhr, R_u, R_rus, R_ex, R_ref, R_ref_COMMA, R_exi, R_m1dash,
    GG,
    #G_trn, G_mrj, G_u, G_rus, G_ex, G_ref, G_ref_COMMA,
    Out])


if __name__ == '__main__':
    import igraph
    g = igraph.Graph(directed=True)
    for s in sm.states:
        g.add_vertex(s, label=s)
    for s in sm.states:
        for t in sm.states:
            if hasattr(sm.states[s], t):
                g.add_edge(s, t)
    l = g.layout("circle")
    visual_style = {}
    visual_style["vertex_color"] = "yellow"
    visual_style["vertex_size"] = "30"
    visual_style["edge_color"] = "black"
    visual_style["vertex_shape"] = "circle"
    visual_style["bbox"] = (1000, 1000)
    igraph.plot(g, layout=l, margin=100, **visual_style)
