def letters_change_numbers(strings):
    total_sum = 0

    for string in strings:
        number_in_between = int(string[1:len(string) - 1])

        if string[0].isupper():
            divided = number_in_between / (ord(string[0]) - 64)

            if string[-1].isupper():
                subtract_from_divided = divided - (ord(string[-1]) - 64)
                total_sum += subtract_from_divided
            elif string[-1].islower():
                added_to_divided = divided + (ord(string[-1]) - 96)
                total_sum += added_to_divided

        elif string[0].islower():
            multiplied = number_in_between * (ord(string[0]) - 96)

            if string[-1].isupper():
                subtract_from_multiplied = multiplied - (ord(string[-1]) - 64)
                total_sum += subtract_from_multiplied
            elif string[-1].islower():
                added_to_multiplied = multiplied + (ord(string[-1]) - 96)
                total_sum += added_to_multiplied

    print(f"{total_sum :.2f}")


texts = input().split()
letters_change_numbers(texts)






