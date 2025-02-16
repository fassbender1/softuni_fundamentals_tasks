def palindromes(palindrome_list: list, compare: str):
    list_palindromes = []
    match_found = 0

    for word in palindrome_list:
        if word == "".join(reversed(word)):
            list_palindromes.append(word)
        if word == compare:
            match_found += 1

    return list_palindromes, match_found


list_of_words = input().split()
palindrome_word = input()
result = palindromes(list_of_words, palindrome_word)
print(f"{result[0]}\nFound palindrome {result[1]} times")