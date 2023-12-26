import os
import re
from math import prod
import day03_lib as lib

INPUT_FILENAME = "input_03.txt"


def extract_gears(line_matrix: [], char_matrix: [[]]):
    gears = {}
    for x in range(len(line_matrix)):
        line = line_matrix[x]
        num_spans = [m.span() for m in re.finditer(r'\d+', line)]
        for num_span in num_spans:
            adj_xy = lib.get_adjacent_xy(x, num_span, char_matrix)
            if adj_xy: gears.setdefault(adj_xy, []).append(int(line[num_span[0]:num_span[1]]))
    gears = {k: v for k, v in gears.items() if len(v) > 1}
    return gears


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    line_matrix = lib.gen_line_matrix(input_filepath)
    char_matrix = lib.gen_char_matrix(input_filepath)
    gears = extract_gears(line_matrix, char_matrix)
    print("Ratios produces: ", sum(list(prod(v) for k, v in gears.items())))


if __name__ == "__main__":
    main()
