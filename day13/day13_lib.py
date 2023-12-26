import os

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file:
        patterns = [[line for line in pattern.split()] for pattern in file.read().split("\n\n")]
    return patterns

def count_diff(left, right: list):
    return len([(i,j) for i,j in zip(left, right) if i!=j])

def find_mirror(pattern: list, num_smudge: int):
    for c in range(1, len(pattern[0])):
        total_diff = 0
        for r in range(len(pattern)):
            left = pattern[r][:c][::-1]
            right = pattern[r][c:]
            m = min(len(left), len(right))
            total_diff += count_diff(left[:m], right[:m])
        if total_diff == num_smudge: return c
    return 0