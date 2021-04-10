from unittest import TestCase

from orders.coffee import Coffee
from orders.menu import Menu


class TestMenu(TestCase):
    LATTE_ID = 1
    ESPRESSO_ID = 2
    AMERICANO_ID = 3

    def test_add_items(self):
        latte = Coffee(id=self.LATTE_ID,
                       name='latte',
                       price=4000)
        espresso = Coffee(id=self.ESPRESSO_ID,
                          name='espresso',
                          price=2000)
        americano = Coffee(id=self.AMERICANO_ID,
                           name='americano',
                           price=500)

        menu = Menu()
        coffee_list = [latte, espresso, americano]
        menu.add_items(coffee_list)

        for coffee in coffee_list:
            expected = {
                'name': coffee.name,
                'price': coffee.price
            }
            self.assertEqual(expected, menu.product_list[coffee.id])

        menu.add_items([latte])
        self.assertEqual(3, len(menu.product_list))
        for coffee in coffee_list:
            expected = {
                'name': coffee.name,
                'price': coffee.price
            }
            self.assertEqual(expected, menu.product_list[coffee.id])

    def test_get_items(self):
        latte = Coffee(id=self.LATTE_ID,
                       name='latte',
                       price=4000)
        espresso = Coffee(id=self.ESPRESSO_ID,
                          name='espresso',
                          price=2000)
        americano = Coffee(id=self.AMERICANO_ID,
                           name='americano',
                           price=500)

        menu = Menu()
        coffee_list = [latte, espresso, americano]
        menu.add_items(coffee_list)

        self.assertEqual(sorted(coffee_list, key=lambda x: x.id), menu.get_items())
