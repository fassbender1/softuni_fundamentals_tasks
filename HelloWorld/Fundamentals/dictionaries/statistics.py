class Statistics:

    def __init__(self):
        self.stock = {}

    def add_create_products(self, command):
        while True:

            if command == "statistics":
                break

            product, quantity = command.split(": ")
            quantity = int(quantity)

            if product in self.stock:
                self.stock[product] += quantity
            else:
                self.stock[product] = quantity

            command = input()

    def products_in_stock(self):
        product_count = len(self.stock)
        products_quantity = sum(self.stock.values())
        print(f"Products in stock:")
        for product, quantity in self.stock.items():
            print(f"- {product}: {quantity}")
        print(f"Total Products: {product_count}")
        print(f"Total Quantity: {products_quantity}")


key_value_pairs = input()
statistics = Statistics()
statistics.add_create_products(key_value_pairs)
statistics.products_in_stock()

