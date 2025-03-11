text = input().split()

repeat = ""

for word in text:
    iterations = len(word)
    repeat += word * iterations

print(repeat)