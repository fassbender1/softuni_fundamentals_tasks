def pass_validator(passwd):

    digit_count = 0
    is_letter_digit = bool
    print_list = []

    for char in passwd:
        if not char.isalpha() and not char.isdigit():
            is_letter_digit = False
            break

    for char in passwd:
        if char.isdigit():
            digit_count += 1

    if len(passwd) < 6 or len(passwd) > 10:
        length = f"Password must be between 6 and 10 characters"
        print_list.append(length)

    if not is_letter_digit:
        letter = f"Password must consist only of letters and digits"
        print_list.append(letter)

    if digit_count < 2:
        digits = f"Password must have at least 2 digits"
        print_list.append(digits)

    if not print_list:
        valid = f"Password is valid"
        print_list.append(valid)

    return print_list


password = input()
result = pass_validator(password)
print(*result, sep="\n")
