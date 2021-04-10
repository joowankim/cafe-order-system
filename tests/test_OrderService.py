from collections import namedtuple
from unittest import TestCase

from orders.coffee import Coffee
from orders.coffeeRepository import CoffeeRepository
from orders.menu import Menu
from orders.orderService import OrderService


class TestOrderService(TestCase):
    LATTE_ID = 1
    ESPRESSO_ID = 2
    AMERICANO_ID = 3

    def test_get_menu(self):
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

        coffee_repo = CoffeeRepository()

        Stock = namedtuple(typename='Stock', field_names=['id', 'count'])

        expected = []
        for coffee in coffee_list:
            cnt = 1
            stock = Stock(coffee.id, cnt)
            coffee_repo.put(stock)
            expected.append({
                'id': coffee.id,
                'name': coffee.name,
                'price': coffee.price,
                'amount': stock.count
            })

        order_service = OrderService(coffee_repo, menu)

        self.assertEqual(expected, order_service.get_menu())


