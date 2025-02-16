def merge(list_string, current_command):
    start_index, end_index = int(current_command[1]), int(current_command[2])
    if start_index not in range(len(list_string)):
        start_index = 0
    if end_index not in range(len(list_string)):
        end_index = len(list_string) - 1
    list_string[start_index] = "".join(list_string[start_index:end_index + 1])
    list_string = list_string[: start_index + 1] + list_string[end_index + 1:]

    return list_string


def divide(string_list, some_command):
    index, partitions = int(some_command[1]), int(some_command[2])
    element = string_list[index]
    partition_size = len(element) // partitions
    partitioned_element = []
    number_of_partition = 0
    for current_index in range(0, len(element), partition_size):
        number_of_partition += 1
        if number_of_partition == partitions:
            current_partition = element[current_index:]
            partitioned_element.append(current_partition)
            break
        else:
            current_partition = element[current_index:current_index + partition_size]
            partitioned_element.append(current_partition)
    string_list = string_list[:index] + partitioned_element + string_list[index + 1:]

    return string_list


string = input().split()
command = input()
while command != "3:1":
    command = command.split()
    action = command[0]
    if action == "merge":
        string = merge(string, command)
    elif action == "divide":
        string = divide(string, command)

    command = input()

print(" ".join(string))

