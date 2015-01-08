class SimpleBNFError(Exception):
    pass


def simple_bnf(grammar, data):
    if isinstance(grammar['data'], dict):
        data = simple_bnf(grammar['data'], data)
    elif isinstance(grammar['data'], list):
        data = map(simple_bnf, grammar['data'], data)
    else:
        if data != grammar['data']:
            raise SimpleBNFError('expected: "{0}", got: "{1}"'.format(grammar['data'], data))
    return {'name': grammar['name'], 'data': data}
