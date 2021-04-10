from collections import namedtuple
from unittest import TestCase

from orders.coffee import Coffee
from orders.coffeeRepository import CoffeeRepository
from orders.menu import Menu


Stock = namedtuple(typename='Stock', field_names=['id', 'count'])


class BaseTest(TestCase):
    LATTE_ID = 1
    ESPRESSO_ID = 2
    AMERICANO_ID = 3

    def setUp(self):
        self.latte = Coffee(id=self.LATTE_ID,
                       name='latte',
                       price=4000)
        self.espresso = Coffee(id=self.ESPRESSO_ID,
                          name='espresso',
                          price=2000)
        self.americano = Coffee(id=self.AMERICANO_ID,
                           name='americano',
                           price=500)

        self.menu = Menu()
        self.coffee_list = [self.latte, self.espresso, self.americano]
        self.menu.add_items(self.coffee_list)

        self.coffee_repo = CoffeeRepository()

        for coffee in self.coffee_list:
            cnt = 1
            stock = Stock(coffee.id, cnt)
            self.coffee_repo.put(stock)
