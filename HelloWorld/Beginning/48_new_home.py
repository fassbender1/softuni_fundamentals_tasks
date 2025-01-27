# Съществуват следните отстъпки:
# · Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# · Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;
# · Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# · Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# · Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# Да се отпечата на конзолата на един ред:
# · Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# · Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

flowers_type = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if flowers_type == "Roses":
    price = 5 * number_of_flowers
elif flowers_type == "Dahlias":
    price = 3.80 * number_of_flowers
elif flowers_type == "Tulips":
    price = 2.80 * number_of_flowers
elif flowers_type == "Narcissus":
    price = 3 * number_of_flowers
elif flowers_type == "Gladiolus":
    price = 2.50 * number_of_flowers

if number_of_flowers > 80 and flowers_type == "Roses":
    price *= 0.90
elif number_of_flowers > 90 and flowers_type == "Dahlias":
    price *= 0.85
elif number_of_flowers > 80 and flowers_type == "Tulips":
    price *= 0.85
elif number_of_flowers < 120 and flowers_type == "Narcissus":
    price += price * 0.15
elif number_of_flowers < 80 and flowers_type == "Gladiolus":
    price += price * 0.20

if price <= budget:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers_type} and {money_left :.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed :.2f} leva more.")
