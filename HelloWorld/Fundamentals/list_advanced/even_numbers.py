def even_numbers(numbers):
    found_even_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
    even_indexes = list(filter(lambda a: a != "no", found_even_or_no))
    return even_indexes


string_of_nums = list(map(int, input().split(", ")))
result = even_numbers(string_of_nums)
print(result)