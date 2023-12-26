import day19_lib as lib
from day19_lib import Condition, OPERATORS

INPUT_FILENAME = "input_19.txt"

def is_condition_meet(condition: Condition, rating: dict):
    if condition.simple: return True
    return OPERATORS[condition.comparsion](rating[condition.key], condition.value)

def is_accepted(rating, workflows: dict):
    name = "in"
    while name != "A" and name != "R":
        rules = workflows[name]
        for condition in rules:
            if is_condition_meet(condition, rating):
                name = condition.target
                break
    return name == "A"

def main():
    workflows, ratings = lib.parse_input(INPUT_FILENAME)
    print("Result: ", sum([sum(rating.values()) for rating in ratings if is_accepted(rating, workflows)]))

if __name__ == "__main__":
    main()