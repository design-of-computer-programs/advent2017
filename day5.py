from utilities import vector

#offsets = list(vector("0 3 0 1 -3"))

offsets = [int(line) for line in open('data/day5.txt')]

index = step = next_index = 0

while next_index in range(len(offsets)):
    next_index = index + offsets[index]
    offsets[index] += (-1 if offsets[index] >= 3 else 1)
    #offsets[index] += 1
    step += 1
    index = next_index

print(step)
