import day09_lib as lib

INPUT_FILENAME = "input_09.txt"

def main():
    num_matrix = lib.parse_input(INPUT_FILENAME)
    num_matrix = [nums[::-1] for nums in num_matrix]
    print(sum(lib.calc_diff(nums) for nums in num_matrix))


if __name__ == "__main__":
    main()