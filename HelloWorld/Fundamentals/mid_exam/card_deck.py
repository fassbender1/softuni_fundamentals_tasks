def card_deck(card_list, number_of_iterations):

    for _ in range(number_of_iterations):
        command = input().split(", ")
        action = command[0]

        if action == "Add":
            card = command[1]
            if card not in card_list:
                card_list.append(card)
                print(f"Card successfully added")
            else:
                print(f"Card is already in the deck")
        elif action == "Remove":
            card = command[1]
            if card not in card_list:
                print(f"Card not found")
            else:
                card_list.remove(card)
                print(f"Card successfully removed")
        elif action == "Remove At":
            index_to_remove = int(command[1])
            index_of_cards_in_deck = list(map(int, (index for index in range(len(card_list)))))
            if index_to_remove not in index_of_cards_in_deck:
                print(f"Index out of range")
            else:
                card_list.pop(index_to_remove)
                print(f"Card successfully removed")
        elif action == "Insert":
            index_to_insert = int(command[1])
            card = command[2]
            index_of_cards_in_deck = list(map(int, (index for index in range(len(card_list)))))
            if card not in card_list:
                if index_to_insert not in index_of_cards_in_deck:
                    print(f"Index out of range")
                else:
                    card_list.insert(index_to_insert, card)
                    print(f"Card successfully added")
            else:
                if index_to_insert not in index_of_cards_in_deck:
                    print(f"Index out of range")
                else:
                    print(f"Card is already added")

    print(", ".join(card for card in card_list))


string_of_cards = input().split(", ")
num_of_commands = int(input())
result = card_deck(string_of_cards, num_of_commands)


