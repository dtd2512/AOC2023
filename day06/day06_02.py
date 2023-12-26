import os
import re

INPUT_FILENAME = "input_06.txt"

def parse_input(input_filepath: str):
    with open(input_filepath) as file:
        lines = file.read().splitlines()
    times = int("".join(re.findall(r'\d+', lines[0])))
    distances = int("".join(re.findall(r'\d+', lines[1])))
    print(times, distances)
    return times, distances


def count_possibilities(time, distance: int):
    c = 0
    for i in range(1, time):
        if i * (time - i) > distance: c += 1
    return c


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    times, distances = parse_input(input_filepath)
    print(count_possibilities(times, distances))


if __name__ == "__main__":
    main()
