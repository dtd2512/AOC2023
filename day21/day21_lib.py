import os
from enum import Enum
from functools import reduce
from math import gcd

class POINT():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, d: tuple):
        return POINT(self.x + d[0], self.y + d[1])
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, o):
        if self and o: return self.x == o.x and self.y == o.y
        return False

    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
DIRS = (UP, DOWN, LEFT, RIGHT)

def is_in_maze(point: POINT, maze: tuple, ):
    return point.x >= 0 and point.x < len(maze) and point.y >= 0 and point.y < len(maze[0])

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file:
        rows = tuple(line.rstrip() for line in file.readlines())
        for i,row in enumerate(rows):
            if "S" in row: s_point = POINT(i, row.index("S"))
    return s_point, rows
