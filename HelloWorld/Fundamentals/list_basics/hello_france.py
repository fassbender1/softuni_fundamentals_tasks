# max_prices = {"Clothes": 50.00, "Shoes": 35.00, "Accessories": 20.50}
# items_type_price_input = input()
# budget = float(input())
#
# items_type_price = items_type_price_input.split("|")
# profit = 0
# bought_items = []
# initial_budget = budget
#
# for types in items_type_price:
#     item, price = types.split("->")
#     price = float(price)
#
#     if item in max_prices and price <= max_prices[item] and budget >= price:
#             budget -= price
#             bought_items.append(price)
#
# new_prices = [round(price * 1.4, 2) for price in bought_items]
# earned_money = sum(new_prices)
# profit = earned_money - sum(bought_items)
# budget += earned_money
#
# print(" ".join(f"{price:.2f}" for price in new_prices))
# print(f"Profit: {profit :.2f}")
#
# if budget >= 150:
#     print(f"Hello, France!")
# else:
#     print(f"Not enough money.")
#
#
#

items_type_price = input().split("|")
budget = float(input())

boosted_prices = []
profit = 0

for types in items_type_price:
    parts = types.split("->")
    item = parts[0]
    price = float(parts[1])
    if item == "Clothes":
        if price <= 50.00 and price <= budget:
            budget -= price
            boosted_prices.append(price * 1.4)
            profit += price * 0.4
    elif item == "Shoes":
        if price <= 35.00 and price <= budget:
            budget -= price
            boosted_prices.append(price * 1.4)
            profit += price * 0.4
    elif item == "Accessories":
        if price <= 20.50 and price <= budget:
            budget -= price
            boosted_prices.append(price * 1.4)
            profit += price * 0.4

for new_price in boosted_prices:
    budget += new_price

print(" ".join(f"{price :.2f}" for price in boosted_prices))
print(f"Profit: {profit :.2f}")

if budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")