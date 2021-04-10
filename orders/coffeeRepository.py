from collections import defaultdict


class NegativeIntegerError(ValueError):
    def __init__(self, value):
        super().__init__(f"Amount of {value} cannot be negative")


class CoffeeRepository:
    def __init__(self):
        self.inventory = defaultdict(int)

    def put(self, choice):
        if choice.count < 0:
            raise NegativeIntegerError("coffee")
        changes = {choice.id: self.inventory.get(choice.id, 0) + choice.count}
        self.inventory.update(changes)

    def get_inventory(self):
        return self.inventory
