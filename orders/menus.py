from orders.VO.coffee import Coffee


class Menu:
    def __init__(self, products: dict):
        self.products = products

    def get_coffee_info(self, name) -> Coffee:
        return self.products.get(name, Coffee("Espresso", 2000))
