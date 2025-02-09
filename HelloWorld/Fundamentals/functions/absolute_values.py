# def absolute_values():
#
#
# absolute_values()

numbers_sequence = input().split()

list_of_numbers = []

for number in numbers_sequence:
    list_of_numbers.append(abs(float(number)))

print(f"{list_of_numbers}")