import os
import re
import day03_lib as lib

INPUT_FILENAME = "input_03.txt"


def extract_part_num(line_matrix: [], char_matrix: [[]]):
    part_nums = []
    for x in range(len(line_matrix)):
        line = line_matrix[x]
        num_spans = [m.span() for m in re.finditer(r'\d+', line)]
        for num_span in num_spans:
            if lib.is_adjacent(x, num_span, char_matrix): part_nums.append(int(line[num_span[0]:num_span[1]]))
    return part_nums


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    line_matrix = lib.gen_line_matrix(input_filepath)
    char_matrix = lib.gen_char_matrix(input_filepath)
    part_nums = extract_part_num(line_matrix, char_matrix)
    print("Sum part numbers: ", str(sum(part_nums)))


if __name__ == "__main__":
    main()
