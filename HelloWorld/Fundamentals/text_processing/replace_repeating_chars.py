def replace_chars(string):
    filtered = ""
    last_added_char = ""
    for char in text:
        if char != last_added_char:
            filtered += char
            last_added_char = char

    return filtered


text = input()
result = replace_chars(text)
print(result)