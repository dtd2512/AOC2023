import os
from functools import lru_cache

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    records = []
    with open(input_filepath) as file: 
        for line in file:
            tokens = line.rstrip().split()
            springs = tokens[0]
            conditions = tuple(map(int, tokens[1].split(",")))
            records.append((springs, conditions))
    return records


def is_valid_group(springs, conditions: tuple):
    if "." in springs[:conditions[0]]: return False     # no split in a #-group
    if len(springs) > conditions[0]:                    # 
        if springs[conditions[0]] == "#": return False  # the character next to a #-group is not allowed to be # (should be . or ?)
    elif len(springs) < conditions[0]:                  #
        return False                                    # num of #-characters should be smaller or equal the springs string
    return True


# LRU Cache & Recursion
# https://www.pythoninformer.com/programming-techniques/functional-programming/recursion/
@lru_cache(maxsize=128)
def count_arrangements(springs, conditions: tuple):
    if not springs: return not conditions               # when reaching the end of the springs string, the conditions should be empty
    if not conditions: return "#" not in springs        # when there are no more conditions then there should be no more #-groups in the spring string
    count = 0
    if springs[0] == ".":
        count += count_arrangements(springs[1:], conditions)
    elif springs[0] == "#":
        if is_valid_group(springs, conditions): count += count_arrangements(springs[conditions[0] + 1:], conditions[1:])
    else:
        count += count_arrangements(springs[1:], conditions)
        if is_valid_group(springs, conditions): count += count_arrangements(springs[conditions[0] + 1:], conditions[1:])
    return count
