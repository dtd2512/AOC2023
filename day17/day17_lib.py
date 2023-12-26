import os
from heapq import heappush, heappop

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
    
    def __lt__(self, o):
        if self and o: return self.x < o.x and self.y < o.y
        return False
    
    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)
    
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIR = [UP, DOWN, LEFT, RIGHT]

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file:
        return [list(int(c) for c in list(line.strip())) for line in file]

def is_in_grid(point: POINT, grid: tuple):
    return point.x >= 0 and point.x < len(grid) and point.y >= 0 and point.y < len(grid[0])

def add(queue, heat_loss:int, S:POINT, dir:tuple, grid:list, steps:int=1):
    N = S.add(dir)
    if not is_in_grid(N, grid): return
    heappush(queue,(
            heat_loss + grid[N.x][N.y],
            N, dir[0], dir[1], steps,
        ),
    )

