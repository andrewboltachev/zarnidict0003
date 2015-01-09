from functools import wraps
import re


def ensure_iterator(f):
    @wraps(f)
    def g(tokens):
        if not hasattr(tokens, '__next__'):
            tokens = iter(tokens)
        return f(tokens)
    return g

def is_opening_tag(x):
    return re.match(r'^\[[a-z]+\]$', x) is not None


def is_closing_tag(x):
    return re.match(r'^\[\/[a-z]+\]$', x) is not None


@ensure_iterator
def f(tokens):
    try:
        token = next(tokens)
    except StopIteration:
        return []
    if token == '[pre]':
        result = f(tokens)
        return [{'name': 'pre', 'data': result}] + f(tokens)
    elif token == '[/pre]':
        return []
    else:
        return [token] + f(tokens)
