def odd_and_even(n1):
    odd_sum = 0
    even_sum = 0
    for each_num_as_str in str(n1):
        each_str_as_num = int(each_num_as_str)
        if each_str_as_num % 2 == 0:
            even_sum += each_str_as_num
        elif each_str_as_num % 2 != 0:
            odd_sum += each_str_as_num
    return odd_sum, even_sum


number = int(input())
result = odd_and_even(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")

