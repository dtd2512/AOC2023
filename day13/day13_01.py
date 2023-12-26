import day13_lib as lib
from functools import partial

INPUT_FILENAME = "input_13.txt"

def main():
    patterns = lib.parse_input(INPUT_FILENAME)
    result = 0
    result += sum(list(map(partial(lib.find_mirror, num_smudge=0), patterns))) 
    result += sum(list(map(partial(lib.find_mirror, num_smudge=0), [list(zip(*pattern)) for pattern in patterns]))) * 100
    print("Result: ", result)


if __name__ == "__main__":
    main()