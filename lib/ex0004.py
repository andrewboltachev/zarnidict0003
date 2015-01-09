class StateMachineError(Exception):
    pass


class State(object):
    def __init__(self, state_machine):
        self.state_machine = state_machine


class StateMachine(object):
    def __init__(self, states):
        self.states = {state.__name__: state(self) for state in states}
        self.initial = self.states[states[0].__name__]

    def run(self, seq):
        self.state = self.initial
        for item in seq:
            if hasattr(self.state, item['name']):
                getattr(self.state, item['name'])(item['data'])
                self.state = self.states[item['name']]
            else:
                raise StateMachineError('No way from {0} to {1}'.format(self.state.__name__, item['name']))
