import copy
import abc

def safe_list_get(t, idx, default):
    l = list(t)
    try:
        return l[idx]
    except IndexError:
        return default


def tail_length(iterator):
    new_iterator = copy.deepcopy(iterator)
    length = 0
    while True:
        try:
            next(new_iterator)
            length += 1
        except StopIteration:
            return length


class AutomatonException(Exception):
    pass


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
    def check_args(self, args):
        for arg in args:
            if not issubclass(arg.__class__, Automaton):
                raise AutomatonException('{0} isn\'t subclass of Automaton'.format(repr(arg)))

    def __init__(self, *args, name=None):
        self.check_args(args)
        self.args = args
        self.name = name

    def run(self, data):
        data, result = self.process(data)
        tail = []
        while True:
            try:
                tail.append(next(data))
            except StopIteration:
                break
        if len(tail):
            raise AutomatonException("Not all input consumed during processing. Tail is: {0}".format(repr(tail)))
        else:
            return result

    @abc.abstractmethod
    def process(self, data):
        pass

    def node(self, data):
        return self.node_class(data, name=self.name, klass=self.__class__.__name__)

    @property
    def edn_value(self):
        return list(map(self._x_to_edn_like, self.args))

    @property
    def edn_payload(self):
        return self.name

    def to_edn_like(self):
        return {
            'type': self.__class__.__name__,
            'value': self.edn_value,
            'payload': self.edn_payload,
        }

    @classmethod
    def _x_to_edn_like(self, x):
        if issubclass(x.__class__, Automaton):
            return x.to_edn_like()
        else:
            return x


class Char(Automaton):
    def check_args(self, args):
        pass

    @property
    def edn_value(self):
        return self._x_to_edn_like(self.args[0])

    @property
    def edn_payload(self):
        return safe_list_get(self.args, 1, None)

    def process(self, data):
        c = copy.deepcopy(data)
        try:
            next_char = next(c)
        except StopIteration:
            raise AutomatonException("Wasn't able to consume all line. Tried do match char {0}".format(self.args[0]))
        if next_char.name == self.args[0]:
            return c, next_char
        raise AutomatonException("Char incorrect {0}. Tried to match char {1}".format(next_char.name, self.args[0]))


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
        return data, self.node(seq)


class Or(Automaton):
    def process(self, data):
        variants = []
        errors = []
        for arg in self.args:
            c = copy.deepcopy(data)
            try:
                c, r = arg.process(c)
            except AutomatonException as e:
                errors.append(e)
            else:
                variants.append((c, r))
        if len(variants) == 0:
            c = copy.deepcopy(data)
            try:
                next_char = next(c)
            except StopIteration:
                next_char_desc = "Reached end of input"
            else:
                next_char_desc = "Next char is {0}".format(next_char)
            raise AutomatonException("Wasn't able to resolve Or rule (name={0}).".format(self.name) + next_char_desc + " Received error messages are {0}".format(repr(errors)))
        else:
            variants = sorted(variants, key=lambda x: tail_length(x[0]))
            return variants[0]


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
            except AutomatonException:
                return c, self.node(seq)
            else:
                seq.append(r)
                c = c1

    @property
    def edn_value(self):
        return self._x_to_edn_like(self.args[0])



class MayBe(Automaton):
    node_class = SeqNode
    def process(self, data):
        c = copy.deepcopy(data)
        try:
            c1, r = self.args[0].process(c)
        except StopIteration:
            return c, self.node([])
        except AutomatonException:
            return c, self.node([])
        else:
            return c1, self.node([r])

    @property
    def edn_value(self):
        return self._x_to_edn_like(self.args[0])
