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


def get_tag(x):
    return x.replace('[', '').replace(']', '')


@ensure_iterator
def f(tokens):
    try:
        token = next(tokens)
    except StopIteration:
        return []
    if is_opening_tag(token):
        tag = get_tag(token)
        result = f(tokens)
        return [{'name': tag, 'data': result}] + f(tokens)
    elif is_closing_tag(token):
        return []
    else:
        return [token] + f(tokens)
