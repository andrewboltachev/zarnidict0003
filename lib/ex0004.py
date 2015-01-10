from functools import wraps


class StateMachineError(Exception):
    pass


class State(object):
    def __init__(self, state_machine):
        self.state_machine = state_machine


class StateMachine(object):
    def __init__(self, states):
        self.states = {state.__name__: state(self) for state in states}
        self.initial = self.states[states[0].__name__]
        self.last_state = self.states[states[len(states) - 1].__name__]

    def run(self, seq):
        self.state = self.initial
        for item in seq:
            if hasattr(self.state, item['name']):
                func = getattr(self.state, item['name'])
                func(item['data'])

                if hasattr(func, 'state'):
                    new_state_name = getattr(func, 'state')
                else:
                    new_state_name = item['name']

                self.state = self.states[new_state_name]
            else:
                raise StateMachineError('No way from {0} to {1}'.format(self.state.__class__.__name__, item['name']))
        if hasattr(self.state, self.last_state.__class__.__name__):
            getattr(self.state, self.last_state.__class__.__name__)(None)
            self.state = self.last_state
        if self.state != self.last_state:
            raise StateMachineError('State {0} isn\'t last one. Last state is {1}'.format(self.state.__class__.__name__, self.last_state.__class__.__name__))


def to_state(state):
    def f(func, *args, **kwargs):
        @wraps(func)
        def g(*args, **kwargs):
            return func(*args, **kwargs)
        g.state = state
        return g
    return f


def state_pfx(pfx):
    def f(func, *args, **kwargs):
        @wraps(func)
        def g(*args, **kwargs):
            return func(*args, **kwargs)
        state = getattr(func, 'state', func.__name__)
        g.state = pfx + state
        return g
    return f
