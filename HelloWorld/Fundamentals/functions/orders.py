def orders(product, quantity):
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity


product_type = input()
amount = int(input())
result = orders(product_type, amount)
print(f"{result:.2f}")
