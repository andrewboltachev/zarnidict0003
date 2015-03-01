import sys
def perr(*x):
    sys.stderr.write(' '.join(map(str, x)) + '\n')

def mark_depth(s1, depth=0):
    return {
        'data': list(map(lambda x: mark_depth(x, depth + 1), s1)) if isinstance(s1, list) else s1,
        'depth': depth,
    }


def walk_depth_maked(f, s1):
    perr('there is', s1)
    return {
            'depth': s1['depth'],
            'data': list(map(lambda x: f(walk_depth_maked(f, x)), s1['data'])) if (isinstance(s1['data'], list)) else s1['data']
    }


def walk(inner, outer, form):
    #return list(map(lambda x: f(walk(f, x)), s1)) if (isinstance(s1, list)) else s1
    if (isinstance(form, list)):
        return outer(list(map(inner, form)))
    if (isinstance(form, dict)):
        return outer({k: inner(v) for k, v in form.items() })
    else:
        return outer(form)

def postwalk(f, form):
    return walk(lambda x: postwalk(f, x), f, form)


def f1(ds):
    #counter = 0

    all_of_size = []

    def find_or_create(data):
        if data in all_of_size:
            return all_of_size.index(data)
        else:
            all_of_size.append(data)
            return len(all_of_size) - 1

    def harvester(x, current_depth):
        perr('coming', x)
        if isinstance(x, dict):
            return {'link': find_or_create(x)}
        return x

    r = postwalk(find_or_create, ds)

    def remove_depth(x):
        if isinstance(x, dict):
            if set(x.keys()) == {'depth', 'data'}:
                return x['data']
        return x
    perr('---')
    perr(postwalk(remove_depth, r))
    return list(enumerate(postwalk(remove_depth, all_of_size)))
