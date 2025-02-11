# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица. Резултатът да се изведе форматиран
# до 2 цифри след десетичната точка. При невалиден град или обем на продажбите
# (отрицателно число) да се отпечата "error".

city = input()
sales_range = float(input())

sales_percentage = 0
is_Valid = True

if city == "Sofia":

    if 0 <= sales_range <= 500:
        sales_percentage = 0.05
    elif 500 < sales_range <= 1000:
        sales_percentage = 0.07
    elif 1000 < sales_range <= 10000:
        sales_percentage = 0.08
    elif sales_range > 10000:
        sales_percentage = 0.12
    else:
        is_Valid = False
elif city == "Varna":

    if 0 <= sales_range <= 500:
        sales_percentage = 0.045
    elif 500 < sales_range <= 1000:
        sales_percentage = 0.075
    elif 1000 < sales_range <= 10000:
        sales_percentage = 0.10
    elif sales_range > 10000:
        sales_percentage = 0.13
    else:
        is_Valid = False

elif city == "Plovdiv":

    if 0 <= sales_range <= 500:
        sales_percentage = 0.055
    elif 500 < sales_range <= 1000:
        sales_percentage = 0.08
    elif 1000 < sales_range <= 10000:
        sales_percentage = 0.12
    elif sales_range > 10000:
        sales_percentage = 0.145
    else:
        is_Valid = False

else:
    is_Valid = False

commission_size = sales_range * sales_percentage

if not is_Valid:
    print("error")

else:
    print(f'{commission_size :.2f}')

