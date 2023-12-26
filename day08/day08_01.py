import os
import day08_lib as lib

INPUT_FILENAME = "input_08.txt"


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    lrs, nodes = lib.parse_input(input_filepath)
    print("num_steps: ", lib.count_steps(lrs, nodes, "AAA", lambda s: s == "ZZZ"))


if __name__ == "__main__":
    main()