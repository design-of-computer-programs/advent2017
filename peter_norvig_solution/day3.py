from itertools import cycle
from collections import defaultdict

RIGHT, UP, LEFT, DOWN = (1, 0), (0, 1), (-1, 0), (0, -1)


def _8_neigbors(x, y): return [
        (x-1, y+1), (x, y+1), (x+1, y+1), 
        (x-1, y  ),           (x+1, y  ),
        (x-1, y-1), (x, y-1), (x+1, y-1)
        ]

def sparial():
    x = y = span = 0
    yield(x, y)
    for dx, dy in cycle((RIGHT, UP, LEFT, DOWN)):
        if dx: span += 1
        for _ in range(span):
            x += dx; y += dy
            yield x, y


def distance(x, y): return abs(x) + abs(y)


def sparial_sum():
    position_value = defaultdict(int)
    for x_y in sparial():
        neigbors = _8_neigbors(*x_y)
        position_value[x_y] = sum(position_value[p] for p in neigbors) or 1
        yield position_value[x_y]


N = 361527

#for ii, x_y in enumerate(sparial()):
#    if ii + 1 == N:
#        print(distance(*x_y))
#        break

for value in sparial_sum():
    if value > N: 
        print(value) 
        break
