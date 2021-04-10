from collections import defaultdict


class CoffeeRepository:
    def __init__(self):
        self.inventory = defaultdict(int)

    def put(self, stock):
        changes = {stock.id: self.inventory.get(stock.id, 0) + stock.count}
        self.inventory.update(changes)

    def get_inventory(self):
        return self.inventory
