# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено
# магическо число. Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# · Първи ред – начало на интервала – цяло число в интервала [1...999]
# · Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# · Трети ред – магическото число – цяло число в интервала [1...10000]

first_row = int(input())
second_row = int(input())
magic_number = int(input())

sum_of = 0
combination_number = 0
is_found = False

for first in range(first_row, second_row + 1):
    for second in range(first_row, second_row + 1):
        sum_of = first + second
        combination_number += 1
        if sum_of == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{combination_number} ({first} + {second} = {magic_number})")
else:
    print(f"{combination_number} combinations - neither equals {magic_number}")

# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# · Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o "Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# · Ако не е намерена комбинация отговаряща на условието
# o "{броят на всички комбинации} combinations - neither equals {магическото число}"

