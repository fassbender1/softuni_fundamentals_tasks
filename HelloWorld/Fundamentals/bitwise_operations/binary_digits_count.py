num = int(input())
searched_num = int(input())

count = 0

while num > 0:
    leftover = num % 2
    if searched_num == leftover:
        count += 1
    num //= 2

print(count)