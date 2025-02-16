def no_vowels(word):

    remove_vowels = [letter for letter in word if letter not in ["a", "A", "o", "O", "u", "U", "e", "E", "i", "I"]]
    remove_vowels_string = ''.join(remove_vowels)
    return remove_vowels_string


text = input()
print(no_vowels(text))
