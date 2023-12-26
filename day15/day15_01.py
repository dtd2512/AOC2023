import day15_lib as lib

INPUT_FILENAME = "input_15.txt"

def main():
    sequence = lib.parse_input(INPUT_FILENAME)
    print("Result: ", sum(list(map(lib.hash, sequence))))

if __name__ == "__main__":
    main()