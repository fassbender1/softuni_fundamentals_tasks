def calculator(operation, num1, num2):

    if operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return int(num1 / num2)
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


operator = input()
first_num = int(input())
second_num = int(input())
result = calculator(operator, first_num, second_num)
print(result)
