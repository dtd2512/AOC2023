import os
import copy

class DIR(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def opposite(self):
        return DIR(-self.x, -self.y)
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)


class POINT():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_dir(self, d: DIR):
        return POINT(self.x + d.x, self.y + d.y)

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)

UP = DIR(-1,0)
DOWN = DIR(1,0)
LEFT = DIR(0,-1)
RIGHT = DIR(0,1)

TILE_DIRS = {"|": [UP, DOWN],
             "-": [LEFT, RIGHT],
             "L": [UP, RIGHT],
             "J": [UP, LEFT],
             "7": [DOWN, LEFT],
             "F": [DOWN, RIGHT],
             ".": []}

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    rows = []
    start_point = None
    with open(input_filepath) as file:
        for row in file:
            rows.append(list(row.rstrip()))
    for i,row in enumerate(rows):
        if "S" in row: start_point = POINT(i, row.index("S"))
    return start_point, rows

def print_maze(maze: list):
    for r in range(len(maze)): print("".join(maze[r]))

def save_maze(maze: list, filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, filename)
    with open(input_filepath, 'w') as f:
        for line in maze:
            f.write("".join(line) + "\n")

def get_start_tile(loop_dirs: list):
    return next((k for k,v in TILE_DIRS.items() if loop_dirs[1] in v and loop_dirs[-1].opposite() in v), None)

def get_next_dir(tile: str, cur_dir: DIR):
    return next((d for d in TILE_DIRS[tile] if d != cur_dir.opposite()), cur_dir)

def is_point_valid(point: POINT, maze: list):
    return point.x >= 0 and point.x < len(maze) and point.y >= 0 and point.y < len(maze[0])

def get_maze_tile(point: POINT, maze: list):
    return maze[point.x][point.y] if is_point_valid(point, maze) else None

def get_start_dir(start_point: POINT, maze: list):
    for d in [UP, DOWN, LEFT, RIGHT]:
        p = start_point.add_dir(d)
        t = get_maze_tile(p, maze)
        if list([z for z in TILE_DIRS[t] if d == z.opposite()]): return d

def get_loop(start_point: POINT, maze: list):
    next_point = start_point
    next_dir = get_start_dir(start_point, maze)
    loop = [next_point]
    dirs = [next_dir]
    while True:
        next_point = next_point.add_dir(next_dir)
        if next_point == start_point: return loop, dirs
        next_dir = get_next_dir(get_maze_tile(next_point, maze), next_dir)
        loop.append(next_point)
        dirs.append(next_dir)

def visual_maze_loop(maze, loop_points, loop_dirs: list):
    _maze = copy.deepcopy(maze)
    _maze[loop_points[0].x][loop_points[0].y] = get_start_tile(loop_dirs)
    for i in range(0,len(loop_points)):
        d = loop_dirs[i]
        r,c = loop_points[i].x, loop_points[i].y
        if d == UP:
            if loop_dirs[i-1] == LEFT: _maze[r][c] = "↖"
            elif loop_dirs[i-1] == RIGHT: _maze[r][c] = "↗" 
            else: _maze[r][c] = "↑" 
        elif d == DOWN: 
            if loop_dirs[i-1] == LEFT: _maze[r][c] = "↙"
            elif loop_dirs[i-1] == RIGHT: _maze[r][c] = "↘" 
            else: _maze[r][c] = "↓" 
        elif d == LEFT:
            if loop_dirs[i-1] == UP: _maze[r][c] = "↖"
            elif loop_dirs[i-1] == DOWN: _maze[r][c] = "↙" 
            else: _maze[r][c] = "←"
        elif d == RIGHT:
            if loop_dirs[i-1] == UP: _maze[r][c] = "↗"
            elif loop_dirs[i-1] == DOWN: _maze[r][c] = "↘" 
            else: _maze[r][c] = "→"
    save_maze(_maze, "maze_loop.txt")
    return _maze


def visual_maze_io(maze_loop, loop_points, in_points: list):
    _maze_loop = copy.deepcopy(maze_loop)
    loop_points = set(loop_points)
    in_points = set(in_points)
    for r in range(len(_maze_loop)):
        for c in range(len(_maze_loop[r])):
            p = POINT(r,c)
            if p in in_points:
                _maze_loop[p.x][p.y] = "I"
            elif p not in loop_points: 
                _maze_loop[p.x][p.y] = "O"
    save_maze(_maze_loop, "maze_io.txt")
    return _maze_loop