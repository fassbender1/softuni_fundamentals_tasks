def round_numbers(numbers):
    rounded_list = []
    for num in numbers:
        real_num = float(num)
        rounded_list.append(round(real_num))
    return rounded_list


list_of_nums = input().split(" ")
result = round_numbers(list_of_nums)
print(result)
