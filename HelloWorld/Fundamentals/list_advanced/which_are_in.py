def which_are_in(first, second):
    remaining_list = []
    for first_string in first:
        for second_string in second:
            if first_string in second_string:
                remaining_list.append(first_string)
                break

    return remaining_list


sequence_one = input().split(", ")
sequence_two = input().split(", ")
result = which_are_in(sequence_one, sequence_two)
print(result)

