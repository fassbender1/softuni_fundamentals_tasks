def stock_list(string):
    stock = {}

    for i in range(0, len(string), 2):
        food = string[i]
        quantity = data[i + 1]
        stock[food] = int(quantity)

    return stock


data = input().split()
result = stock_list(data)
print(result)


