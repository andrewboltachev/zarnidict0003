import sys
def perr(*x):
    sys.stderr.write(' '.join(map(str, x)) + '\n')

def walk(inner, outer, form):
    if (isinstance(form, list)):
        return outer(list(map(inner, form)))
    if (isinstance(form, dict)):
        return outer({k: inner(v) for k, v in form.items() })
    else:
        return outer(form)

def postwalk(f, form):
    return walk(lambda x: postwalk(f, x), f, form)


def f1(ds):
    all_of_size = []

    def find_or_create(data):
        if data in all_of_size:
            return all_of_size.index(data)
        else:
            all_of_size.append(data)
            return len(all_of_size) - 1

    r = postwalk(find_or_create, ds)

    def remove_depth(x):
        if isinstance(x, dict):
            if set(x.keys()) == {'depth', 'data'}:
                return x['data']
        return x

    perr(postwalk(remove_depth, r))
    return list(enumerate(postwalk(remove_depth, all_of_size)))
