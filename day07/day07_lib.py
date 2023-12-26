import re
from collections import Counter


def parse_input(input_filepath: str):
    with open(input_filepath) as file:
        lines = file.read().splitlines()
    hbs = []
    for line in lines:
        hand = re.search(r'[\dAKQJT]+', line).group()
        bid = int(re.search(r' [\d]+', line).group())
        hbs.append([hand, bid])
    return hbs


# 6 = five of a kind
# 5 = four of a kind
# 4 = full house
# 3 = three of a kind
# 2 = two pairs
# 1 = one pair
# 0 = highest card
def get_poker_type(hand: str, is_joker_ver: bool):
    cards = Counter(hand)

    if is_joker_ver and "J" in cards:
        num_jokers = cards.pop("J")
        if not cards: return 6
        cards[max(cards, key=cards.get)] += num_jokers

    if 5 in cards.values():
        return 6
    elif 4 in cards.values():
        return 5
    elif 3 in cards.values() and 2 in cards.values():
        return 4
    elif 3 in cards.values():
        return 3
    elif 2 in cards.values():
        _c = Counter(cards.values())
        if 3 in _c.values(): return 1
        return 2
    return 0


def build_ranks(hbs: list(list()), is_joker_ver: bool):
    trans_dict = {"T":"B", "J":"1", "Q":"D", "K":"E", "A":"F"} if is_joker_ver else {"T":"B", "J":"C", "Q":"D", "K":"E", "A":"F"}
    for hb in hbs:
        poker_type = get_poker_type(hb[0], is_joker_ver)
        trans_card = hb[0].translate(hb[0].maketrans(trans_dict))
        hb.extend([poker_type, trans_card])
    hbs.sort(key=lambda k: (k[2], k[3]), reverse=True)
    hbs.reverse()
    [x.pop(3) for x in hbs]