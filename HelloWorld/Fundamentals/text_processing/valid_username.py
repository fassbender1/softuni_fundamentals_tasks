def username_is_valid(name):
    if length_is_valid(name) and symbols_are_valid(name) and redundant_symbols(name):
        return True
    return False


def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def symbols_are_valid(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def redundant_symbols(name):
    if " " in name:
        return False
    return True


usernames = input().split(", ")

for username in usernames:
    if username_is_valid(username):
        print(username)
