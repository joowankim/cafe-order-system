from tests.baseTest import BaseTest


class TestMenu(BaseTest):
    def test_add_items(self):
        for coffee in self.coffee_list:
            expected = {
                'name': coffee.name,
                'price': coffee.price
            }
            self.assertEqual(expected, self.menu.product_list[coffee.id])

        self.menu.add_items([self.latte])
        self.assertEqual(3, len(self.menu.product_list))
        for coffee in self.coffee_list:
            expected = {
                'name': coffee.name,
                'price': coffee.price
            }
            self.assertEqual(expected, self.menu.product_list[coffee.id])

    def test_get_items(self):
        self.assertEqual(sorted(self.coffee_list, key=lambda x: x.id), self.menu.get_items())
