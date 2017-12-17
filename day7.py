from utilities import merge_dict
from utilities import all_equal
from utilities import find_different
from collections import defaultdict

def parse_link_as_leave_to_parent(link):
    parent = link.split()[0]
    leaves = link[link.find('->') + 2: ].strip().split(', ') # it's comma and space here
    return {left: parent for left in leaves}


assert parse_link_as_leave_to_parent("fwft (72) -> ktlj, cntj, xhth") == {"ktlj": "fwft", "cntj": "fwft", "xhth": "fwft"}


def build_leaves_to_parent(fname):
    leaves_to_parents = {}
    arbitray_leave = None
    for line in open(fname):
        if line.find('->') == -1 and arbitray_leave is None: arbitray_leave = line.split()[0]
        if line.find('->') == -1: continue

        leave_to_parent_one_line = parse_link_as_leave_to_parent(line)
        leaves_to_parents = merge_dict(leaves_to_parents, leave_to_parent_one_line)

    return arbitray_leave, leaves_to_parents


def find_root(leave, leaves_to_parents):
    while leave in leaves_to_parents:  # the root will not in leaves_to_parents's keys.
        leave = leaves_to_parents[leave]

    return leave


def get_parents_to_leaves(leaves_to_parents):
    parents_to_leaves = defaultdict(list)
    for leave, parent in leaves_to_parents.items(): 
        parents_to_leaves[parent].append(leave)
    return parents_to_leaves


def get_weights(fname):
    return {s.split()[0]: int(s[s.find('(')+1: s.find(')')]) for s in open(fname)}


def get_weights_all_tower(root, tree, weights_map):
    if root not in tree: return weights_map[root]
    else: return weights_map[root] + sum([
            get_weights_all_tower(c, tree, weights_map) for c in tree[root]
        ])


def get_unblance_sub_tree(root, tree, weights_map):
    have_seen = [root]
    
    while len(have_seen) > 0:
        r = have_seen.pop(0)
        if r not in tree: break
        else:
            leaves = tree[r]
            weights = [get_weights_all_tower(l, tree, weights_map) for l in leaves]            
            if all_equal(weights):
                have_seen += leaves
            else:
                different_one, normal_one = find_different(weights)
                print(weights)
                return different_one - normal_one

    return 0


puzzle_example = 'data/day7_test.txt'
assert find_root(*build_leaves_to_parent(puzzle_example)) == 'tknk'

tmp_leave, tmp_leaves_to_parents = build_leaves_to_parent(puzzle_example)
tmp_tree = get_parents_to_leaves(tmp_leaves_to_parents)
tmp_weights = get_weights(puzzle_example)
t_root = find_root(*build_leaves_to_parent(puzzle_example)) 

assert get_weights_all_tower('ugml', tmp_tree, tmp_weights) == 251
assert get_weights_all_tower('padx', tmp_tree, tmp_weights) == 243
assert get_weights_all_tower('fwft', tmp_tree, tmp_weights) == 243
assert get_weights_all_tower('tknk', tmp_tree, tmp_weights) == 243 + 243 + 251 + tmp_weights[t_root]

assert get_unblance_sub_tree(t_root, tmp_tree, tmp_weights) == 8


## main

puzzle_input = 'data/day7.txt'
arbitary_leave, leaves_to_parents = build_leaves_to_parent(puzzle_input)
root = find_root(arbitary_leave, leaves_to_parents)
print(root)

tree = get_parents_to_leaves(leaves_to_parents)
weights = get_weights(puzzle_input)
print(get_unblance_sub_tree(root, tree, weights))
