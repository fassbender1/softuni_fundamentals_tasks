import sys

number_range = int(input())

biggest_number_in_range = -sys.maxsize
smallest_number_in_range = sys.maxsize

for _ in range(number_range):
    input_number = int(input())

    if input_number > biggest_number_in_range:
        biggest_number_in_range = input_number

    if input_number < smallest_number_in_range:
        smallest_number_in_range = input_number

print(f"Max number: {biggest_number_in_range}")
print(f"Min number: {smallest_number_in_range}")
