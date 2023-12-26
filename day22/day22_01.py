import day22_lib as lib

INPUT_FILENAME = "input_22.txt"

def main():
    bricks = lib.parse_input(INPUT_FILENAME)
    print("Result: ", lib.count_bricks(bricks, True))

if __name__ == "__main__":
    main()