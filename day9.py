from collections import defaultdict



def get_groups(string):
    stack = []
    garbage_stack = []

    G = defaultdict(lambda: [None, None]) #G = {self_begin: [self_end, parent_begin]}

    for ii, c in enumerate(string):
        if c == '{': 
            stack.append(ii)
            continue
        if c == '}': 
            if ii == len(string) - 1: print(stack)
            self_begin = stack.pop(-1)
            if len(stack) > 0: parent_begin = stack[-1]
            else: 
                print('reach end!')
                parent_begin = -1  # it's the outer most bracket
            self_end = ii
            G[self_begin] = [self_end, parent_begin]

    return G


def get_score_of_group(self_begin, groups):
    if self_begin == 0: return 1
    else:
        return 1 + get_score_of_group(groups[self_begin][1], groups)


def delete_ignored(line):
    collected_chars = [line[0]]

    for c in line[1:]:
        if collected_chars[-1] == '!': 
            collected_chars.pop()
        else:
            collected_chars.append(c)

    return ''.join(collected_chars)


def delete_garbage(line):
    collected_chars = []
    
    skip = False

    for c in line:
        if c == '>' and skip: skip = False
        if c == '<' and not skip: skip = True

        if not skip and c != '>': 
            collected_chars.append(c)


    return ''.join(collected_chars)
        

groups = get_groups('{{{},{},{{}}}}')
print(groups)
print(sum(
    get_score_of_group(g_begin, groups) 
    for g_begin in groups))  # for test


print(delete_garbage((delete_ignored('{{<!>},{<!>},{<!>},{<a>}}'))))
print(delete_garbage(delete_ignored('<!!!>>')))
print(delete_garbage(delete_ignored('<{!>}>')))
print(delete_garbage(delete_ignored('{{<!>},{<!>},{<!>},{<a>}}')))

inputs = next(open('data/day9.txt')).strip()  # the line last is \n, dont forget to delete it.
line = delete_ignored(inputs)
line = delete_garbage(line)
groups = get_groups(line)

print(sum(
    get_score_of_group(g_begin, groups) 
    for g_begin in groups))  # for test
