import copy
import abc


class Node(object):
    def __init__(self, content, name=None, klass=None):
        self.content = content
        self.name = name
        self.klass = klass

    def to_tree(self):
        if issubclass(self.content.__class__, Node):
            return [self.content.to_tree()]
        else:
            return self.content

    def __repr__(self):
        return '<{2} {0} class={1}>'.format(repr(self.to_tree()), self.klass, self.__class__.__name__)

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.to_tree() == other.to_tree()
        else:
            return False


class SeqNode(Node):
    def to_tree(self):
        return [x.to_tree() if x is not None else None for x in self.content]


class Automaton(object, metaclass=abc.ABCMeta):
    node_class = Node
    def __init__(self, *args, name=None):
        self.args = args

    @abc.abstractmethod
    def process(self, data):
        pass

    def node(self, data, name=None):
        return self.node_class(data, name=name, klass=self.__class__.__name__)


class Char(Automaton):
    def process(self, data):
        try:
            next_char = next(data)
        except StopIteration:
            return None
        if next_char.name == self.args[0]:
            return self.node(next_char)
        return None


class InputChar(object):
    def __init__(self, name, payload=None):
        self.name = name
        self.payload = payload

    def __eq__(self, other):
        if isinstance(other, InputChar):
            return self.name == other.name
        else:
            return False

    def __repr__(self):
        return '<InputChar {0} ({1})>'.format(self.name, repr(self.payload))


class Seq(Automaton):
    node_class = SeqNode
    def process(self, data):
        seq = []
        for arg in self.args:
            seq.append(arg.process(data))
        seq = list(filter(lambda x: x is not None, seq))
        if len(seq) == len(self.args):
            return self.node(seq)
        return None


class Or(Automaton):
    def process(self, data):
        for arg in self.args:
            c = copy.deepcopy(data)
            r = arg.process(c)
            if r:
                return r
        return None


class Star(Automaton):
    pass
