import day16_lib as lib
from day16_lib import POINT, RIGHT

INPUT_FILENAME = "input_16.txt"

def main():
    layout = lib.parse_input(INPUT_FILENAME)
    print("Result: ", len(lib.get_beams_xy(POINT(0,0), RIGHT, layout)))

if __name__ == "__main__":
    main()