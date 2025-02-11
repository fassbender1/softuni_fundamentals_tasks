
# Известно е, че:
# ⦁	Декорът за филма е на стойност 10% от бюджета.
# ⦁	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

movie_budget = float(input())
number_of_extras = int(input())
clothing_price_per_extra = float(input())

movie_decor = movie_budget * 0.1
costume_price_for_all_extras = number_of_extras * clothing_price_per_extra

if number_of_extras > 150:
    costume_price_for_all_extras *= 0.9

total_price = movie_decor + costume_price_for_all_extras

if total_price > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {(total_price - movie_budget):.2f} leva more.")
elif total_price <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {(movie_budget - total_price):.2f} leva left.")


