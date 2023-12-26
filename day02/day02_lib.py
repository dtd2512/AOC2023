import os
import re

INPUT_FILENAME = "input_02.txt"
RGB_BAG = (12, 13, 14)
R_RE = "\d+ red"
G_RE = "\d+ green"
B_RE = "\d+ blue"


def extract_num(input: str):
    m_num = re.search(r'\d+', input)
    return int(m_num.group()) if m_num else 0


def extract_game_values(input: str): #return: (game_id, num_r, num_g, num_b)
    input = input.rstrip()
    input_tokens = input.split(':')
    if len(input_tokens) != 2: return ()

    g_id = extract_num(input_tokens[0])
    m_r = re.findall(R_RE, input_tokens[1], re.IGNORECASE)
    m_g = re.findall(G_RE, input_tokens[1], re.IGNORECASE)
    m_b = re.findall(B_RE, input_tokens[1], re.IGNORECASE)
    
    num_r = max(map(extract_num, m_r), default=0)
    num_g = max(map(extract_num, m_g), default=0)
    num_b = max(map(extract_num, m_b), default=0)
    return (g_id, num_r, num_g, num_b)