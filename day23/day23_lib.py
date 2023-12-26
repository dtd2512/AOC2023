import os

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

DOWNHILL = {"^": (UP),
            ">": (RIGHT),
            "v": (DOWN),
            "<": (LEFT),
            ".": (UP, DOWN, LEFT, RIGHT)}

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file: map = tuple([line.rstrip() for line in file])
    start = POINT(0,map[0].find("."))
    end = POINT(len(map) - 1,map[-1].find("."))
    return start, end, map

def is_in_map(point: POINT, map: tuple):
    return point.x >= 0 and point.x < len(map) and point.y >= 0 and point.y < len(map[0])

def get_tile(point: POINT, map: tuple):
    return map[point.x][point.y] if is_in_map(point, map) else ""

def downhill(tile: str):
    if tile == "^": return [UP]
    elif tile == "v": return [DOWN]
    elif tile == "<": return [LEFT]
    elif tile == ">": return [RIGHT]
    else: return [UP, DOWN, LEFT, RIGHT]

def set_hike_path(path: list, map: tuple):
    map = list(map)
    path = set(path)
    for r in range(len(map)):
        map[r] = list(map[r])
        for c in range(len(map[r])):
            if POINT(r,c) in path: map[r][c] = "O"
        map[r] = "".join(map[r])
    return tuple(map)

def print_map(map: tuple):
    for r in map: print(r)