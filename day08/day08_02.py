import os
import day08_lib as lib

INPUT_FILENAME = "input_08.txt"


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    lrs, nodes = lib.parse_input(input_filepath)
    start_keys = [k for k in nodes if k[-1] == "A"]
    num_steps = [lib.count_steps(lrs, nodes, start_key, lambda s: s[-1] == "Z") for start_key in start_keys]
    print("num_steps: ", lib.lcm(num_steps))


if __name__ == "__main__":
    main()
