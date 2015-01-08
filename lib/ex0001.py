class SimpleBNFError(Exception):
    pass


class Or(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r


def simple_bnf(grammar, data):
    if isinstance(grammar['data'], dict):
        data = simple_bnf(grammar['data'], data)
    elif isinstance(grammar['data'], list):
        data = map(simple_bnf, grammar['data'], data)
    elif isinstance(grammar['data'], Or):
        match = False
        for x in (grammar['data'].l, grammar['data'].r):
            try:
                match = simple_bnf(x, data)
            except SimpleBNFError:
                pass
        if match is False:
            raise SimpleBNFError('Or expression "{0}" can\'t be resolved on data "{1}"'.format(grammar['data'], data))
        else:
            data = match
    else:
        if data != grammar['data']:
            raise SimpleBNFError('expected: "{0}", got: "{1}"'.format(grammar['data'], data))
    return {'name': grammar['name'], 'data': data}
