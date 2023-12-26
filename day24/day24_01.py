import day24_lib as lib
import numpy as np
from itertools import combinations

INPUT_FILENAME = "input_24.txt"

def is_cross(p1, v1, p2, v2: tuple, min, max: int):
    le1 = lib.build_linear_equation(p1,v1)
    le2 = lib.build_linear_equation(p2,v2)
    x, y = calc_intersection(le1,le2)
    if not x or not y: return False
    t1 = calc_time(x, p1[0], v1[0])
    t2 = calc_time(x, p2[0], v2[0])
    return t1 >= 0 and t2 >= 0 and min <= x <= max and min <= y <= max

def calc_time(s, s0, v: float):
    return (s - s0) / v

def calc_intersection(le1, le2: tuple):
    A = np.array([[le1[0], le1[1]], [le2[0], le2[1]]])
    b = np.array([-le1[2], -le2[2]])
    try: return tuple(np.linalg.solve(A, b))
    except:return (None, None)

def main():
    note = lib.parse_input(INPUT_FILENAME)
    print("Num intersections: ", len([(p1,v1,p2,v2) for (p1,v1),(p2,v2) in combinations(note,2) if is_cross(p1,v1,p2,v2, 200000000000000, 400000000000000)]))

if __name__ == "__main__":
    main()