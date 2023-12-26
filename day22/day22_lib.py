import os
import re
from collections import defaultdict
from itertools import product

class POINT():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, o):
        if self and o: return self.x == o.x and self.y == o.y
        return False

    def __str__(self):
        return "(%s,%s,%s)"%(self.x, self.y, self.z)
    
class BRICK():
    def __init__(self, start: POINT, end: POINT):
        self.start = start
        self.end = end

    def __hash__(self):
        return hash((self.start, self.end))
    
    def __eq__(self, o):
        if self and o: return self.start == o.start and self.end == o.end
        return False

    # def __lt__(self, o):
    #     return self.score < other.score

    def __str__(self):
        return "(%s,%s)"%(self.start, self.end)

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    bricks = []
    with open(input_filepath) as file:
        for line in file.readlines():
            m = tuple(map(int, re.findall(r'[0-9]+', line)))
            bricks.append(BRICK(POINT(m[0],m[1],m[2]), POINT(m[3],m[4],m[5])))
    return bricks

def get_falled_brick(brick: BRICK, highest_z: defaultdict):
    s = brick.start
    e = brick.end
    hz = max(highest_z[(x, y)] for x in range(s.x, e.x + 1) for y in range(s.y, e.y + 1))
    dz = max(s.z - hz - 1, 0)
    return BRICK(POINT(s.x, s.y, s.z - dz), POINT(e.x, e.y, e.z - dz))

def let_brick_fall(bricks: list):
    bricks.sort(key=lambda brick: brick.start.z)
    highest_z = defaultdict(int)
    falled_bricks = []
    num_falls = 0
    for brick in bricks:
        falled_brick = get_falled_brick(brick, highest_z)
        if falled_brick.start.z != brick.start.z: num_falls += 1
        falled_bricks.append(falled_brick)
        xy = list(product(range(brick.start.x, brick.end.x+1), range(brick.start.y, brick.end.y+1)))
        for _xy in xy: highest_z[_xy] = falled_brick.end.z
    return num_falls, falled_bricks

def count_bricks(bricks: list, safety: bool): # safety = True -> part1, else part2
    _, falled_bricks = let_brick_fall(bricks)
    num_bricks = 0
    # test each brick for disintegrating
    for i in range(len(falled_bricks)):
        remain_bricks = falled_bricks[:i] + falled_bricks[i + 1:]
        num_falls, _ = let_brick_fall(remain_bricks)
        if safety:
            if num_falls == 0: num_bricks += 1
        else:
            num_bricks += num_falls
    return num_bricks