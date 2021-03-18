from unittest import TestCase

from orders.VO.coffee import Coffee


class TestCoffee(TestCase):
    def test_coffee_equals(self):
        first = Coffee("Americano", 3000)
        second = Coffee("Americano", 3000)
        third = Coffee("Americano", 3000)
        other = Coffee("Latte", 4000)

        self.assertTrue(first == first)

        self.assertTrue(first == second)
        self.assertTrue(second == first)

        self.assertTrue(first == second)
        self.assertTrue(second == third)
        self.assertTrue(first == third)

        self.assertNotEqual(first, other)
