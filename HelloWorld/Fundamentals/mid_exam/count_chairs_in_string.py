text = input()
dictionary = {}

for letter in text:
    if letter == " ":
        continue
    if letter not in dictionary.keys():
        dictionary[letter] = 0
    dictionary[letter] += 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")