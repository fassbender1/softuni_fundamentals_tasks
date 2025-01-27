text = input()

point = 0

for char in text:
    if char == "a":
        point += 1
    elif char == "e":
        point += 2
    elif char == "i":
        point += 3
    elif char == "o":
        point += 4
    elif char == "u":
        point += 5

print(point)
