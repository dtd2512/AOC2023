import day18_lib as lib
from day18_lib import DIR

INPUT_FILENAME = "input_18.txt"

def build_dig_plan_rgb(input: tuple):
    dig_plan = [(0,0)]
    num_boundary_points = 0
    for _, _, color in input:
        d = DIR[color[-1]]
        s = int(color[1:-1], 16)
        r,c = dig_plan[-1]
        dig_plan.append((r + d[0]*s, c + d[1]*s))
        num_boundary_points += s
    return dig_plan[:-1], num_boundary_points

def main():
    input = lib.parse_input(INPUT_FILENAME)
    dig_plan, num_boundary_points = build_dig_plan_rgb(input)
    A = lib.calc_area(dig_plan)
    num_interior_points = lib.get_num_interior_points(A, num_boundary_points)
    print("Result: ", num_interior_points + num_boundary_points)

if __name__ == "__main__":
    main()