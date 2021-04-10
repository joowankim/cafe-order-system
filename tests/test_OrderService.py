from orders.bucket import Bucket
from orders.bucketRepository import BucketRepository
from orders.menu import DoesNotExistItemError
from orders.order import Order
from orders.orderRepository import OrderRepository
from tests.baseTest import BaseTest
from orders.orderService import OrderService, ExceedOnHandError, Choice


class TestOrderService(BaseTest):
    CUSTOMER_ID = 1

    def setUp(self):
        super().setUp()
        bucket = Bucket()
        bucket.put(Choice(self.latte.id, 1))

        self.bucket_repo = BucketRepository()
        self.bucket_repo.update_bucket(self.CUSTOMER_ID, bucket)
        self.order_repo = OrderRepository()

        self.order_service = OrderService(self.coffee_repo, self.bucket_repo, self.order_repo, self.menu)

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

        self.assertEqual(expected, self.order_service.get_menu())

    def test_add_items_to_bucket(self):
        items = [
            Choice(self.latte.id, 1)
        ]
        with self.assertRaises(ExceedOnHandError):
            self.order_service.add_items_to_bucket(self.CUSTOMER_ID, items)

        items = [
            Choice(self.americano.id, 1),
            Choice(self.espresso.id, 1)
        ]
        self.order_service.add_items_to_bucket(self.CUSTOMER_ID, items)

        expected = {
            self.latte.id: 1,
            self.americano.id: 1,
            self.espresso.id: 1
        }
        self.assertEqual(expected, self.bucket_repo.get_bucket(self.CUSTOMER_ID).items)

        with self.assertRaises(DoesNotExistItemError):
            self.order_service.add_items_to_bucket(self.CUSTOMER_ID, [Choice(0, 12)])

    def test_create_order(self):
        bucket = self.bucket_repo.get_bucket(self.CUSTOMER_ID)
        order = self.order_service.create_order(self.CUSTOMER_ID, bucket)
        self.assertEqual(self.CUSTOMER_ID, order.customer_id)
        self.assertEqual(bucket, order.bucket)
