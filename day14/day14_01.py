import day14_lib as lib

INPUT_FILENAME = "input_14.txt"

def main():
    dish = lib.parse_input(INPUT_FILENAME)
    north_dish = lib.tilt_north(dish)
    total_load = sum(row.count("O") * (len(north_dish) - i) for i, row in enumerate(north_dish))
    print("Total load: ", total_load)

if __name__ == "__main__":
    main()