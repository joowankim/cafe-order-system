from collections import defaultdict


class NegativeIntegerError(ValueError):
    def __init__(self, value):
        super(NegativeIntegerError, self).__init__(f"Amount of {value} cannot be negative")


class Bucket:
    def __init__(self):
        self.items = defaultdict(int)

    def put(self, choice):
        if choice.count < 0:
            raise NegativeIntegerError("coffee")
        changes = {choice.id: self.items.get(choice.id, 0) + choice.count}
        self.items.update(changes)

    def get_item(self, item_id):
        return self.items.get(item_id, 0)

    def get_cost(self, menu):
        item_prices = []
        for item_id, cnt in self.items.items():
            item_prices.append(menu.get_item(item_id)['price'] * cnt)
        return sum(item_prices)
