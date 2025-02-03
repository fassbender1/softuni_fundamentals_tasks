number = int(input())

is_Prime = True

for i in range(2, number):
    if (number % i) == 0:
        is_Prime = False
        break

print(is_Prime)