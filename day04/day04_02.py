import os
import day04_lib as lib

INPUT_FILENAME = "input_04.txt"


def gen_wining_count_matrix(line_matrix: [str]):
    return list(map(lib.get_wining_count, line_matrix))


def get_wining_cards(card_index:int, count_matrix: [int]):
    if card_index > len(count_matrix): return []
    win_cards = [card_index + 1]
    win_count = count_matrix[card_index]
    for x in range(card_index + 1, card_index + win_count + 1):
        win_cards.extend(get_wining_cards(x, count_matrix))
    return win_cards


def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, INPUT_FILENAME)
    line_matrix = lib.gen_line_matrix(input_filepath)
    wining_count_maxtrix = gen_wining_count_matrix(line_matrix)

    wining_cards = []
    wining_cards.extend(get_wining_cards(i, wining_count_maxtrix) for i in range(len(wining_count_maxtrix)))
    print("wining_cards: ", sum(list(len(x) for x in wining_cards)))


if __name__ == "__main__":
    main()
