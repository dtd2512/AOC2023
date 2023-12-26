import os
import re

INPUT_FILENAME = "input_06.txt"

def parse_input(input_filepath: str):
    with open(input_filepath) as file:
        lines = file.read().splitlines()

    times = list(map(int, re.findall(r'\d+', lines[0])))
    distances = list(map(int, re.findall(r'\d+', lines[1])))
    t2d = {time: distance for time, distance in zip(times, distances)}
    return t2d


def count_possibilities(t2d: dict):
    c = 1
    for t, d in t2d.items():
        p = []
        for i in range(1, t):
            if i * (t - i) > d: p.append(1)
        c *= len(p)
    return c


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    t2d = parse_input(input_filepath)
    print(count_possibilities(t2d))


if __name__ == "__main__":
    main()
