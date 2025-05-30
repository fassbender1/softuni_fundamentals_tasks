class Inventory:

    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity <= len(self.items):
            return f"not enough room in the inventory"
        else:
            self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.get_capacity() - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
