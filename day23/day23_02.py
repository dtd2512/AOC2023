import day23_lib as lib
from day23_lib import POINT
import sys
sys.setrecursionlimit(10000)

INPUT_FILENAME = "input_23.txt"

def DFS(map: tuple, S, E: POINT, seen=[], paths=[]): 
    if S == E: paths.append(seen)
    else:
        P = seen[-1] if seen else None
        seen = seen + [S]
        ST = lib.get_tile(S, map)
        for d in lib.downhill(ST):
            N = S.add(d)
            NT = lib.get_tile(N, map)
            if (NT and NT != "#" and N != P): 
                DFS(map, N, E, seen, paths)
    return paths

def main():
    S, E, map = lib.parse_input(INPUT_FILENAME)
    paths = DFS(map, S, E)

    longest_steps = max([len(path) for path in paths])
    longest_paths = [path for path in paths if len(path) == longest_steps]

    print("Longest hike: ", longest_steps)
    map = lib.set_hike_path(longest_paths[0], map)
    lib.print_map(map)


if __name__ == "__main__":
    main()