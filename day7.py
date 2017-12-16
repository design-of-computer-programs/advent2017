from utilities import merge_dict

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


assert find_root(*build_leaves_to_parent('data/day7_test.txt')) == 'tknk'

print(find_root(*build_leaves_to_parent('data/day7.txt')))



