def mark_depth(s1, depth=0):
    return {
        'data': list(map(lambda x: mark_depth(x, depth + 1), s1)) if isinstance(s1, list) else s1,
        'depth': depth,
    }


def f1(ds):
    #counter = 0

    all_of_size = {}

    def harvester(x):
        if isinstance():
            pass
        return x

    return {0: []}
