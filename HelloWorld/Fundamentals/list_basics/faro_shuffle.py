card_deck = input().split()
shuffle_count = int(input())

for current_shuffle in range(shuffle_count):
    deck_middle = len(card_deck) // 2
    left_deck = card_deck[:deck_middle]
    right_deck = card_deck[deck_middle:]
    deck_after_shuffle = []
    for card_index in range(len(right_deck)):
        deck_after_shuffle.append(left_deck[card_index])
        deck_after_shuffle.append(right_deck[card_index])
    card_deck = deck_after_shuffle.copy()

print(card_deck)
