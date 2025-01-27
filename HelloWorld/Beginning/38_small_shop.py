# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
#
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число), въведени от потребителя,
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

supply = str(input())
city = str(input())
amount = float(input())

if city == "Sofia":
    if supply == "coffee":
        coffee = 0.50
        price = amount * coffee
    elif supply == "water":
        water = 0.80
        price = amount * water
    elif supply == "beer":
        beer = 1.20
        price = amount * beer
    elif supply == "sweets":
        sweets = 1.45
        price = amount * sweets
    elif supply == "peanuts":
        peanuts = 1.60
        price = amount * peanuts
elif city == "Plovdiv":
    if supply == "coffee":
        coffee = 0.40
        price = amount * coffee
    elif supply == "water":
        water = 0.70
        price = amount * water
    elif supply == "beer":
        beer = 1.15
        price = amount * beer
    elif supply == "sweets":
        sweets = 1.30
        price = amount * sweets
    elif supply == "peanuts":
        peanuts = 1.50
        price = amount * peanuts
elif city == "Varna":
    if supply == "coffee":
        coffee = 0.45
        price = amount * coffee
    elif supply == "water":
        water = 0.70
        price = amount * water
    elif supply == "beer":
        beer = 1.10
        price = amount * beer
    elif supply == "sweets":
        sweets = 1.35
        price = amount * sweets
    elif supply == "peanuts":
        peanuts = 1.55
        price = amount * peanuts

print(price)