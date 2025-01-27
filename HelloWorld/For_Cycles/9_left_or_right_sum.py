# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на
# първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

num = int(input())

sum_left_range = 0
sum_right_range = 0

for idx in range(2 * num):
    input_number_left = int(input())
    if idx < num:
        sum_left_range += input_number_left
    else:
        sum_right_range += input_number_left

if sum_left_range == sum_right_range:
    print(f"Yes, sum = {sum_left_range}")
else:
    difference = sum_left_range - sum_right_range
    print(f"No, diff = {abs(difference)}")


