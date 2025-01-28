num_of_lines = int(input())

sum = 0

for i in range(num_of_lines):
    string = input()
    ascii = ord(string)
    sum += ascii

print(f"The sum equals: {sum}")