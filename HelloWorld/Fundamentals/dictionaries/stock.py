class Stock:

    def __init__(self):
        self.in_stock = {}

    def stock_data(self, stocks):
        for i in range(0, len(stocks), 2):
            product = stocks[i]
            quantity = int(stocks[i + 1])
            self.in_stock[product] = quantity

    def products_wanted(self, requested_items):
        for product in requested_items:
            if product in self.in_stock:
                print(f"We have {self.in_stock[product]} of {product} left")
            else:
                print(f"Sorry, we don't have {product}")


key_value = input().split()
product_wanted = input().split()
stock = Stock()
stock.stock_data(key_value)
stock.products_wanted(product_wanted)


