numbers = int(input())

positive_list, negative_list = [], []
positives, negatives_sum = 0, 0

for i in range(numbers):
    next_number = int(input())
    if next_number > 0:
        positive_list.append(next_number)
        positives += 1
    elif next_number < 0:
        negative_list.append(next_number)
        negatives_sum += next_number

print(positive_list)
print(negative_list)
print(f"Count of positives: {positives}")
print(f"Sum of negatives: {negatives_sum}")

