def burger_bus(number):
    number_visited = 0
    money_earned = 0
    total_money_earned = 0

    for num in range(number):
        name_of_city = input()
        earned_money = float(input())
        money_spent = float(input())
        number_visited += 1
        if number_visited % 5 == 0:
            earned_money = earned_money * 0.9
        elif number_visited % 3 == 0:
            money_spent = money_spent * 1.5

        money_earned += (earned_money - money_spent)
        print(f"In {name_of_city} Burger Bus earned {money_earned :.2f} leva.")
        total_money_earned += money_earned
        money_earned = 0

    print(f"Burger Bus total profit: {total_money_earned :.2f} leva.")


number_of_cities = int(input())
result = burger_bus(number_of_cities)
