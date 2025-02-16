def numbers(sequence):
    average = sum(sequence) / len(sequence)
    highest = [num for num in sequence if int(num) > average]
    highest.sort(reverse=True)

    if not highest:
        return "No"
    else:
        return " ".join(map(str, highest[:5]))


string = list(map(int, input().split()))
result = numbers(string)
print(result)