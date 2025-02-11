def evens(numbers):
    even_nums = []
    for num in numbers:
        if int(num) % 2 == 0:
            even_nums.append(int(num))
    return even_nums


list_of_nums = input().split()
result = evens(list_of_nums)
print(result)

# def is_even(number: int) -> bool:
#     return number % 2 == 0
#
#
# list_as_str = input().split()
# list_as_int = []
# for num in list_as_str:
#     list_as_int.append(int(num))
# result = list(filter(is_even, list_as_int))
# print(result)
