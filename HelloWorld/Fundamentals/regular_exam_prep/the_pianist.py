def add_piece(collection_, piece, composer, key):
    if piece in collection_:
        print(f"{piece} is already in the collection!")
    else:
        collection_[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove_piece(collection_, piece):
    if piece in collection_:
        del collection_[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(collection_, piece, new_key):
    if piece in collection_:
        collection_[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def pianist():
    num_of_pieces = int(input())
    collection = {}

    for _ in range(num_of_pieces):
        piece, composer, key = input().split("|")
        collection[piece] = {'composer': composer, 'key': key}

    while True:
        command = input()
        if command == "Stop":
            break

        pieces = command.split("|")
        action = pieces[0]

        if action == "Add":
            add_piece(collection, pieces[1], pieces[2], pieces[3])
        elif action == "Remove":
            remove_piece(collection, pieces[1])
        elif action == "ChangeKey":
            change_key(collection, pieces[1], pieces[2])

    for piece, info in collection.items():
        print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")


pianist()

