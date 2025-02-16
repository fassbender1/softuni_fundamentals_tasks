def numbers(sequence):

    command = input().split()

    while command[0] != "Finish":
        action, value = command[0], command[1]
        if action == "Add":
            sequence.append(value)
        elif action == "Remove":
            # if value in sequence:
            indexes_of_matching_value = list(map(int, (index for index in range(len(sequence)) if value == sequence[index])))
            first_occurrence_index = indexes_of_matching_value[0]
            sequence.pop(first_occurrence_index)
        elif action == "Replace":
            second_value = command[2]
            # if value in sequence:
            indexes_of_matching_value = list(map(int, (index for index in range(len(sequence)) if value == sequence[index])))
            first_occurrence_index = indexes_of_matching_value[0]
            sequence.pop(first_occurrence_index)
            sequence.insert(first_occurrence_index, second_value)
        elif action == "Collapse":
            less_than_value = list(map(int, (num for num in sequence if int(num) < int(value))))
            for num in less_than_value:
                sequence.remove(str(num))

        command = input().split()

    return " ".join(number for number in sequence)


string = input().split()
result = numbers(string)
print(result)
