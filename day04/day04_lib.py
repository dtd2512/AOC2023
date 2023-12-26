import re

def gen_line_matrix(input_filepath: str):
    line_matrix = []
    with open(input_filepath) as file:
        line_matrix = [line.rstrip() for line in file]
    return line_matrix


def get_card_nums(input: str):
    return re.findall(r'\d+', input)


def get_my_nums(input: str):
    return re.findall(r'\d+', input)


def get_wining_count(line: str):
    m = re.match(r'Card +\d+:', line)
    if not m: return 0
    line = line[m.end():]
    tokens = line.split('|')
    if len(tokens) != 2: return 0
    card_nums = get_card_nums(tokens[0])
    my_nums = get_my_nums(tokens[1])
    win_nums = [x for x in my_nums if x in card_nums]
    return len(win_nums)
