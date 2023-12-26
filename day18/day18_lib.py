import os

U = (-1,0)
D = (1,0)
L = (0,-1)
R = (0,1)
DIR = {"U": U, "D": D, "L": L, "R": R, "0": R, "1": D, "2": L, "3": U}

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    input = []
    with open(input_filepath) as file:
        for line in file:
            tokens = line.rstrip().split()
            input.append((tokens[0], int(tokens[1]), tokens[2][1:-1]))
    return tuple(input)

# Shoelace formula is used to calculate the area of a polygon from its xy-points
# https://en.wikipedia.org/wiki/Shoelace_formula
def calc_area(dig_plan: list):
    A = 0
    for i in range(len(dig_plan)):
        p1 = dig_plan[i - 1]
        p2 = dig_plan[i]
        A += p1[0]*p2[1] - p1[1]*p2[0]
    return abs(A)//2

# Pick's theorem is used to calculate the area of a polygon from its interior and boundary points
# https://en.wikipedia.org/wiki/Pick%27s_theorem
def get_num_interior_points(A,b: int):
    return A+1-b//2