def caesar_cipher(string):
    new_string = ""
    for char in string:
        new_char = ord(char) + 3
        new_string += chr(new_char)

    return new_string


text = input()
result = caesar_cipher(text)
print(result)