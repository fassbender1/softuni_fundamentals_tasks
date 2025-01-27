# Магазин за плодове през работните дни работи на следните цени:
# През събота и неделя магазинът работи на по-високи цени:
# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
# · плод - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# · ден от седмицата - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# · количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или
# невалидно име на плод да се отпечата "error".

fruit = input()
day_of_the_week = input()
quantity = float(input())

price = 0

if (day_of_the_week == "Monday"
        or day_of_the_week == "Tuesday"
        or day_of_the_week == "Wednesday"
        or day_of_the_week == "Thursday"
        or day_of_the_week == "Friday"):
    if fruit == "banana":
        price = 2.50
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "apple":
        price = 1.20
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "orange":
        price = 0.85
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "grapefruit":
        price = 1.45
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "kiwi":
        price = 2.70
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "pineapple":
        price = 5.50
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "grapes":
        price = 3.85
        cost = quantity * price
        print(f'{cost :.2f}')
    else:
        print("error")

elif (day_of_the_week == "Saturday"
      or day_of_the_week == "Sunday"):
    if fruit == "banana":
        price = 2.70
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "apple":
        price = 1.25
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "orange":
        price = 0.90
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "grapefruit":
        price = 1.60
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "kiwi":
        price = 3.00
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "pineapple":
        price = 5.60
        cost = quantity * price
        print(f'{cost :.2f}')
    elif fruit == "grapes":
        price = 4.20
        cost = quantity * price
        print(f'{cost :.2f}')
    else:
        print("error")

else:
    print("error")



