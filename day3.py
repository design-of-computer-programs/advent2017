from collections import namedtuple
import operator as op
from itertools import product


def generate_sequence(N, initial_position=(0, 0), initial_value=1): 
    already_position = {}
    next_step = initial_position
    for i in range(N):
        if i != 0:  next_step = generate_next_step(*position, already_position=already_position)

        if i == 0: 
            position_value = initial_value
        else:
            arounds_steps = get_around_positions(*next_step)
            position_value = sum(already_position.get(p, 0) for p in arounds_steps)
            #position_value = i + 1

        already_position[next_step] = position_value
        position = next_step
        yield (position_value, next_step)


def get_around_positions(x, y):
    value = [0, 1, -1]

    arounds = []
    for position in product(value, value):
        x_add, y_add = position
        if x_add != 0 or y_add != 0:
            arounds.append((x + x_add, y + y_add))

    return arounds


def generate_next_step(x, y, already_position=set()): 
    next_possible_step = ((x+1, y), (x, y+1), (x-1, y), (x, y-1))
    next_possible_step = [step for step in next_possible_step if step not in already_position]

    def distance(x, y): return (x + y) * (x + y) - 2 * x * y

    step = min(map(lambda step: (distance(*step), step), next_possible_step), key=lambda x: x[0])[1]

    return step


# target ==> make length longer and closet to center.
assert generate_next_step(0, 0) == (1, 0)
assert generate_next_step(1, -1, already_position=[(1, 0), (0, -1)]) == (2, -1)
assert generate_next_step(1, 0, already_position=[(0, 0)]) == (1, 1)
assert generate_next_step(2, 0, already_position=[(1, 0)]) == (2, 1)

N = 10
G = generate_sequence(N)
#assert next(G) == (1, (0, 0)) #1
#assert next(G) == (1, (1, 0)) #2
#assert next(G) == (2, (1, 1)) #3
#assert next(G)[1] == (0, 1) #4
#assert next(G)[1] == (-1, 1) #5
#assert next(G)[1] == (-1, 0)  #6
#assert next(G)[1] == (-1, -1) #7

assert sorted(get_around_positions(0, 0)) == sorted([(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)])
assert sorted(get_around_positions(-1, -1)) == sorted([(0, 0), (-1, 0), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (0, -1)])

N = 361527
#for step, position in generate_sequence(N):
#    if step % 1000 == 0: 
#        print(step, position)
#    if step == N: 
#        print(abs(position[0]) + abs(position[1]))

# question 2
for value, position in generate_sequence(N):
    if value > N: 
        print(value)
        break
