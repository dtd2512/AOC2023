import os
import day07_lib as lib

INPUT_FILENAME = "input_07.txt"

def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    hbs = lib.parse_input(input_filepath)
    lib.build_ranks(hbs, False)
    print(hbs)
    total_winnings = 0
    for x in range(len(hbs)): total_winnings += (hbs[x][1] * (x+1))
    print("total_winnings: ", total_winnings)


if __name__ == "__main__":
    main()
