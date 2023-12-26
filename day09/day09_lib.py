import os

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file:
        lines = file.read().splitlines()
        return list(list(map(int, line.split())) for line in lines)


def calc_diff(input: list):
    diff = [a - b for a, b in zip(input[1:], input[:-1])]
    if len(set(diff)) == 1: return input[-1] + diff[0]
    return input[-1] + calc_diff(diff)