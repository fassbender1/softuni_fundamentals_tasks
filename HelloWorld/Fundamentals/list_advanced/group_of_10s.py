def group_of_tens(numbers):
    numbers = [int(number) for number in numbers.split(", ")]
    current_group = 10
    while numbers:
        filtered_current_group = [number for number in numbers if number <= current_group]
        print(f"Group of {current_group}'s: {filtered_current_group}")
        current_group += 10
        numbers = [number for number in numbers if number not in filtered_current_group]


string = input()
result = group_of_tens(string)


