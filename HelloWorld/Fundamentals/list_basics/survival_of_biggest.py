list_of_numbers = input().split()
count = int(input())

list_as_integer = []

for num in list_of_numbers:
    list_as_integer.append(int(num))

for i in range(count):
    list_as_integer.remove(min(list_as_integer))

# print(*list_as_integer, sep=', ')

print(", ".join(f"{integer}" for integer in list_as_integer))
