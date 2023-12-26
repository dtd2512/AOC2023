import day10_lib as lib
from day10_lib import POINT

INPUT_FILENAME = "input_10.txt"

# Use nonzero-rule winding to check whether a Point falls within an enclosed curve 
# https://en.wikipedia.org/wiki/Nonzero-rule
def get_io_points(maze_loop, loop_points: list):
    in_points = []
    loop_points = set(loop_points)
    for r in range(len(maze_loop)):
        winding = 0
        tiles = ""
        for c in range(len(maze_loop[r])):
            if POINT(r, c) in loop_points:
                t = lib.get_maze_tile(POINT(r,c), maze_loop)
                if t != "←" and t != "→": tiles += t
                if tiles == "↑" or tiles == "↗↗" or tiles == "↖↖": 
                    winding += 1
                    tiles = ""
                elif tiles == "↓" or tiles == "↙↙" or tiles == "↘↘":
                    winding -= 1
                    tiles = ""
                elif tiles == "↗↘" or tiles == "↘↗" or tiles == "↙↖" or tiles == "↖↙":
                    tiles = ""
            else:
                if winding != 0: in_points.append(POINT(r, c))
    return in_points


def main():
    start_point, maze = lib.parse_input(INPUT_FILENAME)
    loop_points, loop_dirs = lib.get_loop(start_point, maze)
    maze_loop = lib.visual_maze_loop(maze, loop_points, loop_dirs)
    in_points = get_io_points(maze_loop, loop_points)
    maze_io = lib.visual_maze_io(maze_loop, loop_points, in_points)

    lib.print_maze(maze_io)
    print("Num of tiles that are enclosed by the loop: ", len(in_points))
    

if __name__ == "__main__":
    main()