from collections import namedtuple
from unittest import TestCase

from orders.coffee import Coffee
from orders.coffeeRepository import CoffeeRepository


class TestProductRepository(TestCase):
    LATTE_ID = 1
    ESPRESSO_ID = 2
    AMERICANO_ID = 3

    def test_put(self):
        latte = Coffee(id=self.LATTE_ID,
                       name='latte',
                       price=4000)
        espresso = Coffee(id=self.ESPRESSO_ID,
                          name='espresso',
                          price=2000)
        americano = Coffee(id=self.AMERICANO_ID,
                           name='americano',
                           price=500)

        coffee_list = [latte, espresso, americano]
        coffee_repo = CoffeeRepository()

        Stock = namedtuple(typename='Stock', field_names=['id', 'count'])

        expected = {}
        for coffee in coffee_list:
            cnt = 1
            stock = Stock(coffee.id, cnt)
            coffee_repo.put(stock)
            expected[stock.id] = stock.count

        # check inventory after first putting items
        self.assertEqual(expected, coffee_repo.inventory)

        stock = Stock(latte.id, 3)
        coffee_repo.put(stock)
        expected[stock.id] += stock.count

        # check inventory after second putting latte 3 cups
        self.assertEqual(expected, coffee_repo.inventory)
        self.assertNotEqual({}, coffee_repo.inventory)
