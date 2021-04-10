from collections import defaultdict

from orders.coffee import Coffee


class DoesNotExistItemError(ValueError):
    def __init__(self, value):
        super(DoesNotExistItemError, self).__init__(f"item {value} does not exist")


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

    def get_item_name(self, item_id):
        try:
            return self.product_list[item_id]['name']
        except KeyError:
            raise DoesNotExistItemError(item_id)

    def get_item(self, item_id):
        try:
            return self.product_list[item_id]
        except KeyError:
            raise DoesNotExistItemError(item_id)
