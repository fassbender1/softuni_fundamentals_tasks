# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда "NoMoreMoney ".
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана
# до втория знак след десетичната запетая.

deposit = input()

balance = 0

while deposit != "NoMoreMoney":
    deposit_number = float(deposit)
    if deposit_number < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {deposit_number :.2f}")
    balance += deposit_number
    new_deposit = deposit
    deposit = input()

print(f"Total: {balance :.2f}")

