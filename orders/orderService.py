from orders.coffeeRepository import CoffeeRepository
from orders.menu import Menu


class OrderService:
    def __init__(self, repo: CoffeeRepository, menu: Menu):
        self.repo = repo
        self.menu = menu

    def get_menu(self):
        """
        get all of items list in menu

        :return: list of products and amount
        """
        inventory = self.repo.get_inventory()
        items = self.menu.get_items()
        return [{'id': item.id,
                 'name': item.name,
                 'price': item.price,
                 'amount': inventory.get(item.id, 0)}
                for item in items]
