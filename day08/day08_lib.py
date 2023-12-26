import re
from math import gcd
from functools import reduce
from typing import Callable

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)


def count_steps(lrs: str, nodes: dict, start_key: str, is_end_node: Callable[[str], bool]):
    num_steps = 0
    next_key = start_key
    while not is_end_node(next_key):
        next_key = nodes[next_key][lrs[num_steps % len(lrs)] == "R"]
        num_steps += 1
    return num_steps


def parse_input(input_filepath: str):
    with open(input_filepath) as file:
        lines = file.read().splitlines()
    lrs = lines.pop(0)
    nodes = {}
    for line in lines:
        m = re.findall(r'[A-Z0-9]+', line)
        if len(m) == 3: nodes[m[0]] = [m[1], m[2]]
    return lrs, nodes


