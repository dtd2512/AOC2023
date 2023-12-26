import os
from functools import reduce

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file: return tuple(file.read().rstrip().split(","))

def hash(s: str):
    return reduce(lambda v, c: (v + ord(c)) * 17 % 256, s, 0)    