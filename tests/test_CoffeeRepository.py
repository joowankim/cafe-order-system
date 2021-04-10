from tests.baseTest import BaseTest, Stock


class TestCoffeeRepository(BaseTest):
    def test_put(self):
        expected = {}
        for coffee in self.coffee_list:
            cnt = 1
            expected[coffee.id] = cnt

        # check inventory after first putting items
        self.assertEqual(expected, self.coffee_repo.inventory)

        stock = Stock(self.latte.id, 3)
        self.coffee_repo.put(stock)
        expected[stock.id] += stock.count

        # check inventory after second putting latte 3 cups
        self.assertEqual(expected, self.coffee_repo.inventory)
        self.assertNotEqual({}, self.coffee_repo.inventory)
