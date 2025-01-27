# Напишете програма, която чете число n, въведено от потребителя, и отпечатва всички числа ≤ n от редицата:
# 1, 3, 7, 15, 31, ….
# Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1.

number = int(input())

starting_number = 1

while starting_number <= number:
    print(starting_number)
    starting_number = starting_number * 2 + 1