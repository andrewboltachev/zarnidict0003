from functools import wraps

def f(data):
    data_iter = iter(data)
    def g(this, next_func):
        if this == '[pre]':
            seq = []
            this = next_func()
            while (this != '[/pre]'):
                seq.append(this)
                this = g(next_func(), next_func)
            return seq
        else:
            return [this] + g(next_func(), next_func)
    return g(next(data_iter), lambda : next(data_iter))


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
