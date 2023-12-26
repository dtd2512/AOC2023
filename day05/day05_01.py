import os
import day05_lib as lib

INPUT_FILENAME = "input_05.txt"


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    SEEDS, S2S, S2F, F2W, W2L, L2T, T2H, H2L = lib.parse_input(input_filepath)
    scs = [lib.build_seed_chain(s, S2S, S2F, F2W, W2L, L2T, T2H, H2L) for s in SEEDS]
    closest_location = min([sc.location for sc in scs])
    print("closest_location:", closest_location)


if __name__ == "__main__":
    main()
