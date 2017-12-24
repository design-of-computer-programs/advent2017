from collections import defaultdict
from utilities import operations as op

R = defaultdict(int)

modify = {'inc': op['+'], 'dec': op['-']}


for line in open('data/day8.txt'):
    splited = line.split()
    reg, _p, val, _c = splited[0], splited[1], splited[2], splited[4:]
    if op[_c[1]](R[_c[0]], int(_c[2])):  R[reg] = modify[_p](R[reg], int(val))


print(max(R.items(), key=lambda x: x[1]))
