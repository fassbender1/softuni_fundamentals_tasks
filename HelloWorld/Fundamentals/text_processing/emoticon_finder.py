def emoticon(string):
    for index in range(len(string)):
        if string[index] == ":":
            print(f"{string[index]}{string[index+1]}")


text = input()
result = emoticon(text)


