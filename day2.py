from utilities import array
from utilities import first


def get_sum_of_difference(rows):
    return sum([max(row) - min(row) for row in array(rows)])


def get_full_divided(row):
    return first(a//b for a in row for b in row if a > b and a % b == 0)


def get_sum_of_divied_even(rows):
    return sum([get_full_divided(row) for row in array(rows)])


sheets = [
"5 1 9 5",
"7 5 3",
"2 4 6 8",
]

assert get_sum_of_difference(sheets) == 18

assert get_full_divided([5, 9, 2, 8]) == 8/2
assert get_full_divided([9, 4, 7, 3]) == 9/3
assert get_full_divided([3, 8, 6, 5]) == 6/3

print('test done!')

if __name__ == '__main__':
    sheets = [line for line in open('data/day2_sheets.txt')]
    print(get_sum_of_difference(sheets))
    print(get_sum_of_divied_even(sheets))
