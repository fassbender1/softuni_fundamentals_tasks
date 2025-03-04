class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if self.capacity > 0:
            self.capacity -= 1
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage


limit = int(input())
storage_limit = Storage(limit)

for _ in range(limit + 1):
    add_prod = input()
    storage_limit.add_product(add_prod)

print(storage_limit.get_products())

