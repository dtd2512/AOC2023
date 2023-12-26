import os
from collections import deque

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

DIR = {
    "|": {LEFT: (DOWN, UP), RIGHT: (DOWN, UP)},
    "-": {UP: (LEFT, RIGHT), DOWN: (LEFT, RIGHT)},
    "/": {UP: (RIGHT,), DOWN: (LEFT,), LEFT: (DOWN,), RIGHT: (UP,)},
    "\\": {UP: (LEFT,), DOWN: (RIGHT,), LEFT: (UP,), RIGHT: (DOWN,)},
    ".": {},
}

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file: return tuple(line.rstrip() for line in file.readlines())

def is_in_layout(point: POINT, layout: tuple):
    return point.x >= 0 and point.x < len(layout) and point.y >= 0 and point.y < len(layout[0])

def get_beams_xy(S: POINT, dir: tuple, layout: tuple):
    queue = deque([(S, dir)])
    seen = set([(S, dir)])
    while queue:
        S, (dr, dc) = queue.popleft()
        N = S.add((dr, dc))
        if not is_in_layout(N, layout): continue
        for nd in DIR[layout[N.x][N.y]].get((dr, dc), ((dr, dc),)):
            if (N, nd) not in seen:
                queue.append((N, nd))
                seen.add((N, nd))
    return seen

def count_energized_tiles(layout: tuple):
    s1 = [max(get_beams_xy(POINT(i,-1), RIGHT, layout), get_beams_xy(POINT(i,len(layout[0])), LEFT, layout)) for i in range(len(layout))]
    s2 = [max(get_beams_xy(POINT(-1, i), DOWN, layout), get_beams_xy(POINT(len(layout),i), UP, layout)) for i in range(len(layout[0]))]
    return max(len(s) for s in s1+s2)
