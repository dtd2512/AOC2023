import os
import day05_lib as lib

INPUT_FILENAME = "input_05.txt"

S2S, S2F, F2W, W2L, L2T, T2H, H2L = ({},)*7

def gen_seed_ranges(nums: [int]):
    if len(nums) % 2 !=0: return None
    chunks = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    seed_ranges = chunks(nums, 2)
    return seed_ranges


def get_min_loc(seed_range: [int]):
    seed_start = seed_range[0]
    seed_end = seed_start + seed_range[1]
    cur_seed = seed_start
    min_loc = lib.build_seed_chain(cur_seed, S2S, S2F, F2W, W2L, L2T, T2H, H2L).location
    step = 1
    while True:
        cur_seed += step
        if cur_seed == seed_end: 
            return min_loc
        elif cur_seed > seed_end:
            cur_seed -= step
            step = 1
        else:
            cur_loc = lib.build_seed_chain(cur_seed, S2S, S2F, F2W, W2L, L2T, T2H, H2L).location
            if min_loc <= cur_loc: 
                step *= 2
            else:
                if step == 1: min_loc = cur_loc
                cur_seed = cur_seed - step 
                step = 1


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    global S2S, S2F, F2W, W2L, L2T, T2H, H2L 
    SEEDS_INPUT, S2S, S2F, F2W, W2L, L2T, T2H, H2L = lib.parse_input(input_filepath)
    SEED_RANGES = gen_seed_ranges(SEEDS_INPUT)

    min_loc = min(list(map(get_min_loc, SEED_RANGES)))
    print("closest_location:", min_loc)


if __name__ == "__main__":
    main()
