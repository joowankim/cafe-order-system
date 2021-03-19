from datetime import datetime
from unittest import TestCase

from orders.VO.coffee import Coffee
from orders.customers import Customer
from orders.VO.order import Order
from orders.VO.receipt import Receipt
from orders.menus import Menu
from orders.sellers import Seller


class TestSeller(TestCase):
    def test_create_receipt(self):
        americano = Coffee("Americano", 3000)
        espresso = Coffee("Espresso", 2000)
        latte = Coffee("Latte", 4000)
        products = {
            americano.name: americano,
            espresso.name: espresso,
            latte.name: latte
        }

        menu = Menu(products)

        seller = Seller("Jack")
        customer = Customer("Yuni", menu)
        coffee = Coffee("Americano", 3000)

        order = Order(
            customer_info=customer.name,
            product=coffee.name,
            amount=1,
            price=3000,
            ordered=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        expected = Receipt(
            customer_name=order.customer_info,
            seller_name=seller.name,
            product=order.product,
            price=order.price,
            amount=order.amount,
            ordered_date=order.ordered)

        receipt = seller.create_receipt(order=order)
        self.assertEqual(expected, receipt)
