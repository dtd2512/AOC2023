import day16_lib as lib
from day16_lib import POINT
from collections import deque

INPUT_FILENAME = "input_16.txt"

def main():
    layout = lib.parse_input(INPUT_FILENAME)
    print("Result: ", lib.count_energized_tiles(layout))

if __name__ == "__main__":
    main()