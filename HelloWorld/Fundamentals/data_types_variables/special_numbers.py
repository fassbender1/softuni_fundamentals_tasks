num = int(input())

for i in range(1, num + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

