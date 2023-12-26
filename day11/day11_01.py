from itertools import combinations
import day11_lib as lib

INPUT_FILENAME = "input_11.txt"

def main():
    image = lib.parse_input(INPUT_FILENAME)
    galaxies = lib.get_galaxies(image)
    empty_rows, empty_cols = lib.get_empty_rc(image)
    path_length = sum(list([lib.calc_shortest_path(galaxy_pair, empty_rows, empty_cols, 1) for galaxy_pair in combinations(galaxies, 2)]))
    print("path_length: ", path_length)

if __name__ == "__main__":
    main()