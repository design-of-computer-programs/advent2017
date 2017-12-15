from utilities import vector

#offsets = list(vector("0 3 0 1 -3"))

offsets = [int(line) for line in open('data/day5.txt')]

index = step = 0
while True:
    next_index = index + offsets[index]
    if offsets[index] >= 3: offsets[index] -= 1
    else: offsets[index] += 1
    step += 1

    if next_index >= len(offsets): 
        break
    index = next_index
    
    #if step % 1000 == 0: print(step)

print(step)
    

