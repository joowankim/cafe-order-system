from collections import defaultdict


class NegativeIntegerError(ValueError):
    def __init__(self, value):
        super(NegativeIntegerError, self).__init__(f"Amount of {value} cannot be negative")


class Bucket:
    def __init__(self):
        self.items = defaultdict(int)

    def put(self, stock):
        if stock.count < 0:
            raise NegativeIntegerError("coffee")
        changes = {stock.id: self.items.get(stock.id, 0) + stock.count}
        self.items.update(changes)

    def get_item(self, item_id):
        return self.items.get(item_id, 0)

