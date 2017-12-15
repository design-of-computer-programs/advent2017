from utilities import cano
from utilities import mapt


def is_valid_passphrase(string, pre_process_func=lambda x: x):
    words = string.strip().split()
    words = pre_process_func(words)
    return len(words) == len(set(words))


def sort_substrings(words):
    return [''.join(sorted(w)) for w in words]

assert is_valid_passphrase("aa bb cc dd ee")
assert not is_valid_passphrase("aa bb cc dd aa")
assert is_valid_passphrase("aa bb cc dd aaa")


lines = open('data/day4_input.txt')

print(sum([1 for line in lines if is_valid_passphrase(line)]))

lines = open('data/day4_input.txt')
print(sum([ 1 for line in lines if is_valid_passphrase(line, sort_substrings)]))


### peter's solution

def is_unique(elements): return len(elements) == len(set(elements))

lines = open('data/day4_input.txt')
print(sum([1 for line in lines if is_unique(line.split())]))

lines = open('data/day4_input.txt')
print(sum([1 for line in lines if is_unique(mapt(cano, line.split()))]))
