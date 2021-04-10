from collections import defaultdict

from orders.coffee import Coffee


class Menu:
    def __init__(self):
        self.product_list = defaultdict(dict)

    def add_items(self, items):
        changes = {item.id: {'name': item.name,
                             'price': item.price}
                   for item in items}
        self.product_list.update(changes)

    def get_items(self):
        return [Coffee(id=key,
                       name=value.get('name', ''),
                       price=value.get('price', 0))
                for key, value in self.product_list.items()]

