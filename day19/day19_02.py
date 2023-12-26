import day19_lib as lib
import copy
from math import prod

INPUT_FILENAME = "input_19.txt"
MIN_MAX = (1,4000)

def count_combinations(name: str, workflows, ranges: dict):
    if name == "R": return 0
    if name == "A": return prod([max-min+1 for min,max in ranges.values()])

    total = 0
    rule = workflows[name]
    for condition in rule:
        if condition.simple:
            total += count_combinations(condition.target, workflows, ranges)
        else:
            new_range = copy.deepcopy(ranges)
            cur_range = ranges[condition.key]
            if cur_range[0] < condition.value < cur_range[1]:
                if condition.comparsion == "<":
                    new_range[condition.key] = (cur_range[0], condition.value - 1)
                    ranges[condition.key] = (condition.value, cur_range[1])
                else:
                    new_range[condition.key] = (condition.value + 1, cur_range[1])
                    ranges[condition.key] = (cur_range[0], condition.value)
                total += count_combinations(condition.target, workflows, new_range)
    return total

def main():
    workflows, _ = lib.parse_input(INPUT_FILENAME)
    print("Result: ", count_combinations("in", workflows, {"x": MIN_MAX, "m": MIN_MAX, "a": MIN_MAX, "s": MIN_MAX}))

if __name__ == "__main__":
    main()