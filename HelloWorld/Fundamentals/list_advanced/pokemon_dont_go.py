def pokemon(numbers):
    removed_elements = 0

    while numbers:
        index = int(input())

        if index < 0:
            removed_value = int(numbers[0])
            numbers[0] = numbers[-1]
        elif index >= len(numbers):
            removed_value = int(numbers[-1])
            numbers[-1] = numbers[0]
        else:
            removed_value = int(numbers.pop(index))

        removed_elements += removed_value

        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
            if numbers[i] <= removed_value:
                numbers[i] += removed_value
            else:
                numbers[i] -= removed_value

    return removed_elements


sequence = input().split()
result = pokemon(sequence)
print(result)
