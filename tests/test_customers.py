from unittest import TestCase

from orders.coffee import Coffee
from orders.customers import Customer
from orders.menus import Menu
from orders.order import Order


class TestCustomer(TestCase):
    def test_create_order(self):
        americano = Coffee("Americano", 3000)
        espresso = Coffee("Espresso", 2000)
        latte = Coffee("Latte", 4000)
        products = {
            americano.name: americano,
            espresso.name: espresso,
            latte.name: latte
        }
        menu = Menu(products)
        customer = Customer("John", menu)

        expected = Order(
            customer_info=customer.name,
            product=americano.name,
            amount=2,
            price=americano.price
        )
        result = customer.create_order(americano.name, 2)
        self.assertEqual(expected, result)
