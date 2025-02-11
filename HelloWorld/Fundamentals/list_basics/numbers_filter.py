number = int(input())

numbers = []
checked = []

for i in range(number):
    number_input = int(input())
    numbers.append(number_input)

number_type = input()

if number_type == "even":
    for num in numbers:
        if num % 2 == 0:
            checked.append(num)
elif number_type == "odd":
    for num in numbers:
        if num % 2 != 0:
            checked.append(num)
elif number_type == "negative":
    for num in numbers:
        if num < 0:
            checked.append(num)
elif number_type == "positive":
    for num in numbers:
        if num >= 0:
            checked.append(num)

print(checked)
