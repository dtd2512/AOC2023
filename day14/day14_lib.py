import os
from functools import lru_cache

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file: lines = tuple([line.rstrip() for line in file])
    return lines

@lru_cache(maxsize=128)
def tilt_cycle(dish: tuple):
    for _ in range(4):
        dish = tilt_north(dish)
        dish = tuple(map("".join, zip(*dish)))
        dish = tuple(row[::-1] for row in dish)
    return dish

@lru_cache(maxsize=128)
def tilt_north(dish: list):
    dish = tuple(map("".join, zip(*dish)))
    north_dish = []
    for row in dish:
        north_row = ""
        for token in row.split("#"):
            north_row += "O" * token.count("O") + "." * token.count(".") + "#"
        north_dish.append(north_row[:-1])
    north_dish = tuple(map("".join, zip(*north_dish)))
    return north_dish