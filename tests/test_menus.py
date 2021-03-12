from unittest import TestCase

from orders.coffee import Coffee
from orders.menus import Menu


class TestMenu(TestCase):
    def test_get_coffee_info(self):
        americano = Coffee("Americano", 3000)
        espresso = Coffee("Espresso", 2000)
        latte = Coffee("Latte", 4000)
        products = {
            americano.name: americano,
            espresso.name: espresso,
            latte.name: latte
        }

        menu = Menu(products)

        expected = americano
        result = menu.get_coffee_info(americano.name)
        self.assertEqual(expected, result)
