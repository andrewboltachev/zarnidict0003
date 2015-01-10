from lib.ex0004 import State, StateMachine


class In(State):
    def pre(self, data):
        pass


class pre(State):
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

    def Out(self, data):
        pass


def Out(State):
    pass


sm = StateMachine([In, pre, trn, mhr, u, rus, Out])
