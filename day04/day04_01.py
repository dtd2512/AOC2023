import os
import day04_lib as lib

INPUT_FILENAME = "input_04.txt"


def calc_point(line: str):
    win_count = lib.get_wining_count(line)
    return 2**(win_count-1) if win_count > 0 else 0


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    line_matrix = lib.gen_line_matrix(input_filepath)
    pile_point = sum(list(map(calc_point, line_matrix)))
    print("pile_point: ", pile_point)


if __name__ == "__main__":
    main()
