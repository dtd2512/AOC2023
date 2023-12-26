import day21_lib as lib
from day21_lib import POINT
from day21_lib import DIRS
from collections import deque

INPUT_FILENAME = "input_21.txt"

def get_plots(S: POINT, maze: tuple, max_steps: int):
    queue = deque([(S, max_steps)])
    seen = {S}
    plots = set()
    while queue:
        P, steps = queue.popleft()
        if steps % 2 == 0: plots.add(P) # odd steps -> back to same point
        if steps == 0: continue
        for d in DIRS:
            N = P.add(d)
            if (lib.is_in_maze(N, maze) and maze[N.x][N.y] != "#" and N not in seen):
                queue.append((N, steps - 1))
                seen.add(N)
    return plots

def main():
    S, maze = lib.parse_input(INPUT_FILENAME)
    print("Result: ", len(get_plots(S, maze, 64)))

if __name__ == "__main__":
    main()