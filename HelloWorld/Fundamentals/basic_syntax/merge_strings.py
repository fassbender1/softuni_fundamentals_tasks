first_string = input()
second_string = input()

last_printed_string = first_string

for char_original_index in range(len(first_string)):
    left_side = second_string[:char_original_index + 1]
    right_side = first_string[char_original_index + 1:]
    new_string = left_side + right_side
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string

