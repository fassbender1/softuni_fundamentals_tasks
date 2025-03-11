products = {}
prices = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break
    item, price, quantity = command[0], float(command[1]), int(command[2])
    if item not in products.keys():
        products[item] = [price, quantity]
    else:
        products[item][1] += quantity
        products[item][0] = price


for item, (price, quantity) in products.items():
    total_price = price * quantity
    print(f"{item} -> {total_price :.2f}")






