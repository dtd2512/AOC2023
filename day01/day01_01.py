import os
import re

INPUT_FILENAME = "input_01.txt"


def extract_calibration_value(input: str):
    input = input.rstrip()
    m1 = re.search(r'\d', input)
    m2 = re.search(r'\d', input[::-1])
    if m1 and m2: 
        return int(m1.group())*10 + int(m2.group())
    else:
        return 0


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    sum_calibration = 0
    with open(input_filepath) as file:
        for line in file:
            sum_calibration += extract_calibration_value(line)
    print("sum_calibration: " + str(sum_calibration))


if __name__ == "__main__":
    main()
