def min_max_sum(numbers: list):
    return min(numbers), max(numbers), sum(numbers)


list_as_str = input().split()
list_as_int = []
for num in list_as_str:
    list_as_int.append(int(num))
result = min_max_sum(list_as_int)

print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result [2]}")