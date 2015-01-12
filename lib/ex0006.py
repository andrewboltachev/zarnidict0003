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

    def to_json_like(self):
        return {
            'name': self.name,
            'klass': self.klass,
            'content': self.content.to_json_like()
        }

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

    def to_json_like(self):
        return {
            'name': self.name,
            'klass': self.klass,
            'content': [x.to_json_like() if x is not None else None for x in self.content]
        }


class Automaton(object, metaclass=abc.ABCMeta):
    node_class = Node
    def __init__(self, *args, name=None):
        self.args = args
        self.name = name

    def run(self, data):
        return self.process(data)[1]

    @abc.abstractmethod
    def process(self, data):
        pass

    def node(self, data):
        return self.node_class(data, name=self.name, klass=self.__class__.__name__)


class Char(Automaton):
    def process(self, data):
        try:
            next_char = next(data)
        except StopIteration:
            return data, None
        if next_char.name == self.args[0]:
            return data, next_char
        return data, None


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

    def to_tree(self):
        return self

    def to_json_like(self):
        return {
            'name': self.name,
            'payload': self.payload
        }


class Seq(Automaton):
    node_class = SeqNode
    def process(self, data):
        seq = []
        for arg in self.args:
            data, r = arg.process(data)
            seq.append(r)
        seq = list(filter(lambda x: x is not None, seq))
        if len(seq) == len(self.args):
            return data, self.node(seq)
        return data, None


class Or(Automaton):
    def process(self, data):
        for arg in self.args:
            c = copy.deepcopy(data)
            c, r = arg.process(c)
            if r:
                return c, r
        return data, None


class Star(Automaton):
    node_class = SeqNode
    def process(self, data):
        seq = []
        c = copy.deepcopy(data)
        while True:
            try:
                c1, r = self.args[0].process(c)
            except StopIteration:
                return c, self.node([])
            else:
                if r:
                    seq.append(r)
                    c = c1
                else:
                    return c, self.node(seq)
