from utilities import vector
from utilities import argmax

puzzle_banks = vector("10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6")


def get_loop_step(banks):
    seen_before = set(); step = 0

    while banks not in seen_before:
        seen_before.add(banks)  
        max_index = argmax(banks)
        need_collected = banks[max_index]

        banks = list(banks)
        banks[max_index] = 0
        for i in range(need_collected):
            banks[(max_index + i + 1)%len(banks)] += 1
        banks = tuple(banks) # change to tuple in order to could hash and put it in set

        step += 1
    return step, banks


step, have_seen_before = get_loop_step(puzzle_banks)

print(step)  # answer for q1

print(get_loop_step(have_seen_before)[0])
