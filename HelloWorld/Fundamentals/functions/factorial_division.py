def factorial(number):
    for num in range(1, number):
        number *= num
    return number


first_num = int(input())
second_num = int(input())
first_factorial = factorial(first_num)
second_factorial = factorial(second_num)
print(f"{first_factorial / second_factorial :.2f}")