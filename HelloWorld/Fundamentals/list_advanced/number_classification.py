def classification(numbers):
    positives = ", ".join([num for num in numbers if int(num) >= 0])
    negatives = ", ".join([num for num in numbers if int(num) < 0])
    evens = ", ".join([num for num in numbers if int(num) % 2 == 0])
    odds = ", ".join([num for num in numbers if int(num) % 2 != 0])
    return f"Positive: {positives}" \
           f"\nNegative: {negatives}" \
           f"\nEven: {evens}" \
           f"\nOdd: {odds}"


string_of_numbers = input().split(", ")
result = classification(string_of_numbers)
print(result)
