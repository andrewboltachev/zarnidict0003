class SimpleBNFError(Exception):
    pass


def simple_bnf(grammar, data):
    if isinstance(grammar['data'], dict):
        return {'name': grammar['name'], 'data': simple_bnf(grammar['data'], data)}
    elif isinstance(grammar['data'], list):
        return {'name': grammar['name'], 'data': map(simple_bnf, grammar['data'], data)}
    else:
        if data == grammar['data']:
            return {'name': grammar['name'], 'data': data}
        else:
            raise SimpleBNFError('expected: "{0}", got: "{1}"'.format(grammar['data'], data))
