from orders.menus import Menu
from orders.order import Order


class Customer:
    def __init__(self, name: str, menu: Menu):
        self.name = name
        self.menu = menu

    def create_order(self, coffee_name: str, amount: int) -> Order:
        coffee = self.menu.get_coffee_info(coffee_name)
        return Order(
            customer_info=self.name,
            product=coffee.name,
            amount=amount,
            price=coffee.price
        )
