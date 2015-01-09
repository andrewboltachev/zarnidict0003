from functools import wraps

def ensure_iterator(f):
    @wraps(f)
    def g(tokens):
        if not hasattr(tokens, '__next__'):
            tokens = iter(tokens)
        return f(tokens)
    return g

@ensure_iterator
def f(tokens):
    try:
        token = next(tokens)
    except StopIteration:
        return []
    if token == '[pre]':
        result = f(tokens)
        return [{'name': 'pre', 'data': result}] + f(tokens)
    elif token.isalpha():
        return [token] + f(tokens)
    elif token == '[/pre]':
        return []
    else:
        return []
