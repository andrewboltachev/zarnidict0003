import sys
def perr(*x):
    sys.stderr.write(' '.join(map(str, x)) + '\n')

def mark_depth(s1, depth=0):
    return {
        'data': list(map(lambda x: mark_depth(x, depth + 1), s1)) if isinstance(s1, list) else s1,
        'depth': depth,
    }


def walk(f, s1):
    perr('there is', s1)
    return {
            'depth': s1['depth'],
            'data': list(map(lambda x: f(walk(f, x)), s1['data'])) if (isinstance(s1['data'], list)) else s1['data']
    }


def f1(ds):
    #counter = 0

    marked_depth = mark_depth(ds)

    all_of_size = {}

    def find_or_create(depth, data):
        if data in all_of_size[depth]:
            return all_of_size[depth].index(data)
        else:
            all_of_size[depth].append(data)
            return len(all_of_size[depth])

    def harvester(x, current_depth):
        perr('coming', x)
        if isinstance(x, dict):
            depth = x['depth']
            if depth == current_depth:
                if not depth in all_of_size:
                    all_of_size[depth] = []
                return {'depth': x['depth'], 'link': find_or_create(x['depth'], x['data'])}
        return x

    for depth in [4,3,2,1]:
        this_harvester = lambda x: harvester(x, depth)
        r = walk(this_harvester, marked_depth)

    perr(r)
    return all_of_size
