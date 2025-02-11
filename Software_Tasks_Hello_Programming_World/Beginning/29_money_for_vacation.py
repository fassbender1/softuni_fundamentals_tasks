price_for_vacay = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzles_price = number_of_puzzles * 2.60
dolls_price = number_of_dolls * 3
bears_price = number_of_bears * 4.10
minions_price = number_of_minions * 8.20
trucks_price = number_of_trucks * 2

total_toy_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
total_number_toys = number_of_trucks + number_of_puzzles + number_of_minions + number_of_bears + number_of_dolls

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

if total_number_toys >= 50:
    total_toy_price *= 0.75
else:
    total_toy_price == total_toy_price

money_minus_rent = total_toy_price * 0.9

if money_minus_rent >= price_for_vacay:
    money_left = money_minus_rent - price_for_vacay
    print(f"Yes! {money_left:.2f} lv left.")
elif money_minus_rent < price_for_vacay:
    money_not_enough = price_for_vacay - money_minus_rent
    print(f"Not enough money! {money_not_enough:.2f} lv needed.")


# Изход
# На конзолата се отпечатва:
# ⦁	Ако парите са достатъчни се отпечатва:
# ⦁	"Yes! {оставащите пари} lv left."
# ⦁	Ако парите НЕ са достатъчни се отпечатва:
# ⦁	"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
