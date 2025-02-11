def ranges(char1, char2) -> list:
    chars = []
    for current_char_as_number in range(ord(char1) + 1, ord(char2)):
        chars.append(chr(current_char_as_number))
    return chars


first_char = input()
second_char = input()
result = ranges(first_char, second_char)
print(" ".join(result))
