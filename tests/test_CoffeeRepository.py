from orders.coffeeRepository import NegativeIntegerError
from orders.orderService import Choice
from tests.baseTest import BaseTest


class TestCoffeeRepository(BaseTest):
    def test_put(self):
        expected = {}
        for coffee in self.coffee_list:
            cnt = 1
            expected[coffee.id] = cnt

        # check inventory after first putting items
        self.assertEqual(expected, self.coffee_repo.inventory)

        choice = Choice(self.latte.id, 3)
        self.coffee_repo.put(choice)
        expected[choice.id] += choice.count

        # check inventory after second putting latte 3 cups
        self.assertEqual(expected, self.coffee_repo.inventory)
        self.assertNotEqual({}, self.coffee_repo.inventory)

        # check negative count
        with self.assertRaises(NegativeIntegerError):
            self.coffee_repo.put(Choice(self.latte.id, -2))
