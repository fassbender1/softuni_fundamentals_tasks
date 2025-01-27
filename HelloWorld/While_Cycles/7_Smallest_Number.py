# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.

import sys

number = input()

min_number = sys.maxsize

while number != "Stop":
    int_number = int(number)
    if int_number <= min_number:
        min_number = int_number
        number = input()
        continue
    else:
        number = input()

print(min_number)
