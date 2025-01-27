# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.
import sys

number = input()

max_number = -sys.maxsize

while number != "Stop":
    int_number = int(number)
    if int_number >= max_number:
        max_number = int_number
        number = input()
        continue
    else:
        number = input()

print(max_number)