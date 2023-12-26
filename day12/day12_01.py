import day12_lib as lib

INPUT_FILENAME = "input_12.txt"

def main():
    records = lib.parse_input(INPUT_FILENAME)
    springs, conditions = map(tuple, zip(*records))
    arrangement_count = sum(list(map(lib.count_arrangements, springs, conditions)))
    print(arrangement_count)


if __name__ == "__main__":
    main()