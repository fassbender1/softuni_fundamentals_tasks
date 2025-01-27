# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб.
# Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# · Цената за наем на кораба през пролетта е 3000 лв.;
# · Цената за наем на кораба през лятото и есента е 4200 лв.;
# · Цената за наем на кораба през зимата е 2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# · Ако групата е до 6 човека включително - отстъпка от 10%;
# · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
# · Ако групата е от 12 нагоре - отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен -
# тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

group_budget = int(input())
season = input()
fisherman_number = int(input())

price = 0

if season == "Spring":
    price = 3000

    if 0 < fisherman_number <= 6:
        price *= 0.90
    elif 7 <= fisherman_number <= 11:
        price *= 0.85
    elif fisherman_number >= 12:
        price *= 0.75

elif season == "Summer" or season == "Autumn":
    price = 4200

    if 0 < fisherman_number <= 6:
        price *= 0.90
    elif 7 <= fisherman_number <= 11:
        price *= 0.85
    elif fisherman_number >= 12:
        price *= 0.75

elif season == "Winter":
    price = 2600

    if 0 < fisherman_number <= 6:
        price *= 0.90
    elif 7 <= fisherman_number <= 11:
        price *= 0.85
    elif fisherman_number >= 12:
        price *= 0.75

discount = 0.0

if fisherman_number % 2 == 0 and season != "Autumn":
    discount = 0.95
    price *= discount

    if price <= group_budget:
        money_left = group_budget - price
        print(f"Yes! You have {money_left :.2f} leva left.")
    elif price >= group_budget:
        money_needed = price - group_budget
        print(f"Not enough money! You need {money_needed :.2f} leva.")

else:
    if price <= group_budget:
        money_left = group_budget - price
        print(f"Yes! You have {money_left :.2f} leva left.")
    elif price >= group_budget:
        money_needed = price - group_budget
        print(f"Not enough money! You need {money_needed :.2f} leva.")


