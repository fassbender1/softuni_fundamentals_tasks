def decipher(message):

    ascii_list = []
    deciphered_list = []

    for word in message:
        ascii_switch = ""
        for num in word:
            if num.isdigit():
                ascii_switch += num
                word = word.replace(num, "")
        ascii_switch = chr(int(ascii_switch)) + word
        ascii_list.append(ascii_switch)

    for word in ascii_list:
        word_to_list = [letter for letter in word]
        word_to_list[1], word_to_list[-1] = word_to_list[-1], word_to_list[1]
        deciphered_list.append("".join(word_to_list))

    return " ".join(deciphered_list)


string = input().split()
result = decipher(string)
print(result)
