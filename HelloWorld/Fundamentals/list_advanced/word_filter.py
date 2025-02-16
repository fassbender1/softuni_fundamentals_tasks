def word_filter(words):
    evens = [word for word in words if len(word) % 2 == 0]
    return "\n".join(evens)


string = input().split()
result = word_filter(string)
print(result)
