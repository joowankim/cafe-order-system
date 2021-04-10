from tests.baseTest import BaseTest
from orders.orderService import OrderService


class TestOrderService(BaseTest):
    def test_get_menu(self):
        expected = []
        for coffee in self.coffee_list:
            cnt = 1
            expected.append({
                'id': coffee.id,
                'name': coffee.name,
                'price': coffee.price,
                'amount': cnt
            })

        order_service = OrderService(self.coffee_repo, self.menu)

        self.assertEqual(expected, order_service.get_menu())


