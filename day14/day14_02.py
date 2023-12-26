import day14_lib as lib

INPUT_FILENAME = "input_14.txt"

def find_repeat(dish: tuple, max_loop: int):
    tilt_history = {}
    for i in range(max_loop):
        dish = lib.tilt_cycle(dish)
        if dish in tilt_history:
            return tilt_history[dish], i - tilt_history[dish], dish
        else: tilt_history[dish] = i
    return None

def main():
    dish = lib.parse_input(INPUT_FILENAME)
    repeat_offset, repeat_index, repeat_dish = find_repeat(dish, 10**9)
    remain_tilts = (10**9 - repeat_offset - 1) % repeat_index
    for _ in range(remain_tilts):
        repeat_dish =  lib.tilt_cycle(repeat_dish)
    total_load = sum(row.count("O") * (len(repeat_dish) - i) for i, row in enumerate(repeat_dish))
    print("Total load: ", total_load)

if __name__ == "__main__":
    main()