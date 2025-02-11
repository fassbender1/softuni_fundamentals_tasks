# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и проверява дали сред тях съществува
# число, което е равно на сумата на всички останали.
# · Ако има такъв елемент печата "Yes" и на нов ред "Sum = " + неговата стойност
# · Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата
# на останалите (по абсолютна стойност)
import sys

num = int(input())

sum_numbers = 0
max_num = -sys.maxsize

for _ in range(0, num):
    number_input = int(input())
    if number_input > max_num:
        max_num = number_input

    sum_numbers += number_input

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    sum_numbers = sum_numbers - max_num
    print(f"No")
    print(f"Diff = {abs(max_num - sum_numbers)}")
