import day17_lib as lib
from day17_lib import POINT, DIR
from heapq import heappop

INPUT_FILENAME = "input_17.txt"

def count_heat_loss(grid:list):
    seen = set()
    priority_queue = [(0, POINT(0, 0), 0, 0, 0)]
    while priority_queue:
        heat_loss, S, dr, dc, steps = heappop(priority_queue)
        if steps>=4 and S.x==len(grid)-1 and S.y==len(grid[S.x])-1: 
            return heat_loss
        if (S, dr, dc, steps) in seen:continue
        seen.add((S, dr, dc, steps))
        if steps < 10 and (dr, dc) != (0, 0):
            lib.add(priority_queue, heat_loss, S, (dr, dc), grid, steps + 1)
        if steps >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    lib.add(priority_queue, heat_loss, S, (ndr, ndc), grid)

def main():
    grid = lib.parse_input(INPUT_FILENAME)
    print("Result: ", count_heat_loss(grid))

if __name__ == "__main__":
    main()