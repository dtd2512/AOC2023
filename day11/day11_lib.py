import os

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file: lines = [line.rstrip() for line in file]
    return lines

def get_galaxies(image: list):
    return [(r,c) for r in range(len(image)) for c in range(len(image[r])) if image[r][c] == "#"]

def get_empty_rc(image: list):
    transpose_image = list(zip(*image))
    empty_rows = set([r for r in range(len(image)) if "#" not in image[r]])
    empty_cols = set([c for c in range(len(transpose_image)) if "#" not in transpose_image[c]])
    return empty_rows, empty_cols

def calc_shortest_path(galaxy_pair: tuple, empty_rows, empty_cols: set, expand_factor: int):
    expand_factor -= expand_factor > 1
    (r1,c1), (r2,c2) = galaxy_pair
    if galaxy_pair == ((0, 3), (8, 7)):
        print("zzz")
    expand_row = len(list([r for r in range(min(r1,r2), max(r1,r2)) if r in empty_rows])) * expand_factor
    expand_col = len(list([c for c in range(min(c1,c2), max(c1,c2)) if c in empty_cols])) * expand_factor
    return abs(r1-r2) + abs(c1-c2) + expand_row + expand_col
