from collections import Counter
import operator as op

operations = {
        "==": op.eq, '!=': op.ne,
        "<=": op.le, '<': op.lt, 
        '>=': op.ge, '>': op.gt,
        "+": op.add, '-': op.sub,
    }


def mapt(func, iterator):
    return tuple(map(func, iterator))


def array(lines, t=int):
    if isinstance(lines, str): lines = lines.splitlines()
    return mapt(vector, lines)


def vector(line):
    return mapt(atom, line.replace(',', ' ').strip().split())


def atom(token):
    try: 
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


def first(iterator):
    return next(iter(iterator))


cat = ''.join

def cano(items, typ=None):
    typ = typ or (cat if isinstance(items, str) else tuple)
    return typ(sorted(items))


def arg_(items, func):
    return func(enumerate(items), key=lambda x: x[1])[0]

def argmax(items): return arg_(items, max)

def argmin(items): return arg_(items, min)


def merge_dict(dict1, dict2):
    return {**dict1, **dict2}


def all_equal(items):
    return len(set(items)) == 1


def find_different(items):
    # return a tuple which contains difference_one and normal_one
    assert len(set(items)) == 2 and len(items) >= 3

    for item, times in Counter(items).items():
        if times == 1: return item, list(set(items) - {item})[0]
    return None, None



assert find_different([1, 2, 2]) == (1, 2)
assert find_different([3, 3, 2]) == (2, 3)

assert all_equal([1, 1, 1])
assert not all_equal([2, 1, 1])

assert merge_dict({1: 1, 2: 2}, {'1': 1, '2': 2}) == {1: 1, 2: 2, '1': 1, '2': 2}

assert argmin([0, 1, 2, 3]) == 0
assert argmin([2, 1, 2, 3]) == 1
assert argmin([2, 1, 1, 3]) == 1
assert argmax([2, 1, 1, 3]) == 3
assert argmax([4, 1, 1, 3]) == 0
assert argmax([2, 5, 5, 3]) == 1

assert mapt(int, ['1', '2', '3']) == (1, 2, 3)

assert atom("1") == 1
assert atom("1.0") == 1.0
assert atom("X") == 'X'

assert vector("5 1 9 5") == (5, 1, 9, 5)
assert vector("5 1 9 5\n") == (5, 1, 9, 5)
assert vector("5.0 1.0 9.0 5.0\n") == (5.0, 1.0, 9.0, 5.0)
assert vector("5.0, 1.0, 9.0, 5.0\n") == (5.0, 1.0, 9.0, 5.0)

assert first("abc") == 'a'


assert array([
    "5 1 9 5",
    "7 5 3",
    "2 4 6 8",
    ]) == ((5, 1, 9, 5), (7, 5, 3), (2, 4, 6, 8))

assert cano('abc') == cano('acb')
assert cano('acb') == 'abc'
assert cano([1, 3, 2]) == (1, 2, 3)
assert cano([1, 3, 2]) == cano([1, 2, 3])
assert cano([1, 3, 2]) != cano([3, 2, 3])

