from collections import OrderedDict


class Star(object):
    def __init__(self, args):
        self.args = list(args)

class Or(object):
    def __init__(self, *args):
        self.args = list(args)


def Plus(a):
    return [a, Star(a)]


def get_first_terminal(g):
    #return OrderedDict([(k, v[0]) for k, v in g.items()])
    return {g.name: g.args}


class Expr(object):
    def __init__(self, name, *args):
        self.name = name
        self.args = list(args)
