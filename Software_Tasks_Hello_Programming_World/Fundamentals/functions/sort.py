def sorteded(numbers: list):
    return sorted(numbers)


list_of_nums = input().split()
list_as_int = []
for num in list_of_nums:
    list_as_int.append(int(num))
result = sorteded(list_as_int)
print(result)
