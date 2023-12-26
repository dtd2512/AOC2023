import day10_lib as lib
from day10_lib import POINT

INPUT_FILENAME = "input_10.txt"

def main():
    start_point, maze = lib.parse_input(INPUT_FILENAME)
    loop_points, loop_dirs = lib.get_loop(start_point, maze)
    maze_loop = lib.visual_maze_loop(maze, loop_points, loop_dirs)
    
    lib.print_maze(maze_loop)
    print("Num steps: ", len(loop_points)//2)


if __name__ == "__main__":
    main()