from collections import defaultdict


class NegativeIntegerError(ValueError):
    def __init__(self, value):
        super().__init__(f"Amount of {value} cannot be negative")


class CoffeeRepository:
    def __init__(self):
        self.inventory = defaultdict(int)

    def put(self, stock):
        if stock.count < 0:
            raise NegativeIntegerError("coffee")
        changes = {stock.id: self.inventory.get(stock.id, 0) + stock.count}
        self.inventory.update(changes)

    def get_inventory(self):
        return self.inventory
