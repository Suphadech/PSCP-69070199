'''Card'''
card_name = input().upper()
card_group = card_name[:-1]
card_symbol = card_name[-1]

card_groups = {
    "A": "ace",
    "J": "jack",
    "K": "king",
    "Q": "queen"
}

card_symbols = {
    "D": "diamonds",
    "H": "hearts",
    "S": "spades",
    "C": "clubs"
}
card_group = card_groups.get(card_group, card_group)
card_symbol = card_symbols[card_symbol]
print(f'{card_group} of {card_symbol}')
