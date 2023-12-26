import os
import re

INPUT_FILENAME = "input_01.txt"
DIGIT_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def word_to_digit(input: str):
    try:
        return int(DIGIT_WORDS.index(input)) + 1
    except:
        return 0


def extract_calibration_value(input: str):
    input = input.rstrip().lower()
    m = re.findall(r"(?=("+'|'.join(DIGIT_WORDS)+'|\d'+r"))", input)
    if m:
        m1 = m[0]
        m2 = m[-1]
        m1 = word_to_digit(m1) if m1 in DIGIT_WORDS else int(m1)
        m2 = word_to_digit(m2) if m2 in DIGIT_WORDS else int(m2)
        return int(m1)*10 + int(m2)
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
