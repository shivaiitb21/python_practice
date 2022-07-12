def locate_card(cards, query):
    pos = 0
    while pos<len(cards):
        if cards[pos] == query:
            return pos
        pos += 1
    return -1

