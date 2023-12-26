import day15_lib as lib
import re
from collections import defaultdict

INPUT_FILENAME = "input_15.txt"

def build_lens(sequence: tuple):
    return tuple(next(iter(re.findall(r"([a-z]+)(=|-)(\d)?", s))) for s in sequence)

def arrange_boxes(lens: tuple):
    boxes = defaultdict(list)
    for l, o, f in lens:
        h = lib.hash(l)
        i = next((_i for _i, item in enumerate(boxes[h]) if item[0] == l), -1)
        if o == "=":
            if i >= 0: 
                boxes[h][i] = (l, f)
            else:
                boxes[h].append((l, f))
        else:
            if i >= 0: del boxes[h][i]
    return boxes

def main():
    sequence = lib.parse_input(INPUT_FILENAME)
    lens = build_lens(sequence)
    boxes = arrange_boxes(lens)
    print("Result: ", sum(list((i+1)*j*int(lf[1]) for i, lfs in boxes.items() for j, lf in enumerate(lfs, start=1))))

if __name__ == "__main__":
    main()