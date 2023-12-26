import day21_lib as lib
from day21_lib import POINT
from day21_lib import DIRS
from collections import deque
import numpy as np

INPUT_FILENAME = "input_21.txt"

def get_plots_ex(S: POINT, maze: tuple, max_steps: int):
    queue = deque([(S, max_steps)])
    seen = {(S, 0, 0)}
    plots = set()
    R = len(maze)
    C = len(maze[0])
    while queue:
        P, steps = queue.popleft()
        if steps % 2 == 0: plots.add(P) # odd steps -> back to same point
        if steps == 0: continue
        for d in DIRS:
            N = P.add(d)
            n_exr, nr = divmod(N.x, R)
            n_exc, nc = divmod(N.y, C)
            if (maze[nr][nc] != "#" and (N,n_exr,n_exc) not in seen):
                queue.append((N, steps - 1))
                seen.add((N, n_exr, n_exc))
    return plots

# Use extrapolation to estimate the num of plots
# https://en.wikipedia.org/wiki/Extrapolation
def extrapolate_plots(S: POINT, maze: tuple, max_steps: int):
    R = len(maze)
    p1 = len(get_plots_ex(S, maze, S.x))
    p2 = len(get_plots_ex(S, maze, S.x + R))
    p3 = len(get_plots_ex(S, maze, S.x + R*2))
    poly = np.rint(np.polynomial.polynomial.polyfit([0, 1, 2], [p1, p2, p3], 2)).astype(int).tolist()
    n = max_steps // R
    return sum(poly[i] * n**i for i in range(3))

def main():
    S, maze = lib.parse_input(INPUT_FILENAME)
    print("Result: ", extrapolate_plots(S, maze, 26501365))

if __name__ == "__main__":
    main()