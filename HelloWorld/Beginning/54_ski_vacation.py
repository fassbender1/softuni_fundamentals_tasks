# Атанас решава да прекара отпуската си в Банско и да кара ски. Преди да отиде обаче, трябва да резервира хотел и
# да изчисли колко ще му струва престоя. Налични са следните видове помещения, със следните цени за престой:
# § "room for one person" – 18.00 лв за нощувка
# § "apartment" – 25.00 лв за нощувка
# § "president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще
# избере, той може да ползва различно намаление.
# След престоя, оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.
# Вход

days = int(input())
accommodation = input()
evaluation = input()

room_for_one = 18.00
apartment = 25.00
president_suite = 35.00
price = 0

if accommodation == "room for one person":
    days -= 1
    price = room_for_one * days

elif accommodation == "apartment":
    days -= 1
    price = apartment * days
    if days < 10:
        price *= 0.70
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.50

elif accommodation == "president apartment":
    days -= 1
    price = president_suite * days
    if days < 10:
        price *= 0.90
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.80


if evaluation == "positive":
    price += price * 0.25
    print(f"{price:.2f}")
else:
    price *= 0.90
    print(f"{price:.2f}")

# Изход
# На конзолата трябва да се отпечата един ред:
# · Цената за престоят му в хотела, форматирана до втория знак след десетичната запетая.
