import os
import day02_lib as lib02

INPUT_FILENAME = "input_02.txt"
RGB_BAG = (12, 13, 14)


def is_game_valid(input: ()):
    if len(input) != 4: return False
    if input[1] > RGB_BAG[0] or input[2] > RGB_BAG[1] or input[3] > RGB_BAG[2]: return False
    return True


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    sum_id = 0
    with open(input_filepath) as file:
        for line in file:
            game_val = lib02.extract_game_values(line)
            if is_game_valid(game_val): sum_id += game_val[0]
    print("sum_id: " + str(sum_id))


if __name__ == "__main__":
    main()
