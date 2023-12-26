ADJ_DIRECTIONS = [[-1,-1,],[-1,0,],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]


def is_valid_xy(x, y, n, m: int):
    if (x < 0 or y < 0 or x > n - 1 or y > m - 1):
        return False
    return True


def is_symbol(x, y: int, char_matrix: [[]]):
    try:
        c = char_matrix[x][y]
        if c != '.' and not c.isdigit(): return True
    except:
        return False
    return False


def is_adjacent(x: int, num_span: [], char_matrix: [[]]):
    return True if get_adjacent_xy(x, num_span, char_matrix) else False


def get_adjacent_xy(x: int, num_span: [], char_matrix: [[]]):
    if x < 0 or x > len(char_matrix) - 1: return False 
    m = len(char_matrix)
    n = len(char_matrix[x])
    for y in range(num_span[0],num_span[1]):
        for d in ADJ_DIRECTIONS:
            adj_x = x + d[0]
            adj_y = y + d[1]
            if is_valid_xy(adj_x, adj_y, m, n) and is_symbol(adj_x, adj_y, char_matrix): return (adj_x, adj_y)
    return None


def gen_char_matrix(input_filepath: str):
    char_matrix = [[]]
    with open(input_filepath) as file:
        char_matrix = [[c for c in line.rstrip()] for line in file]
    return char_matrix


def gen_line_matrix(input_filepath: str):
    line_matrix = []
    with open(input_filepath) as file:
        line_matrix = [line.rstrip() for line in file]
    return line_matrix


