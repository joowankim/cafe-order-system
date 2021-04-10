from orders.bucket import Bucket
from orders.bucketRepository import BucketRepository
from orders.menu import DoesNotExistItemError
from tests.baseTest import BaseTest
from orders.orderService import OrderService, ExceedOnHandError, Stock


class TestOrderService(BaseTest):
    CUSTOMER_ID = 1

    def setUp(self):
        super().setUp()
        bucket = Bucket()
        bucket.put(Stock(self.latte.id, 1))

        self.bucket_repo = BucketRepository()
        self.bucket_repo.update_bucket(self.CUSTOMER_ID, bucket)

        self.order_service = OrderService(self.coffee_repo, self.bucket_repo, self.menu)

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
            Stock(self.latte.id, 1)
        ]
        with self.assertRaises(ExceedOnHandError):
            self.order_service.add_items_to_bucket(self.CUSTOMER_ID, items)

        items = [
            Stock(self.americano.id, 1),
            Stock(self.espresso.id, 1)
        ]
        self.order_service.add_items_to_bucket(self.CUSTOMER_ID, items)

        expected = {
            self.latte.id: 1,
            self.americano.id: 1,
            self.espresso.id: 1
        }
        self.assertEqual(expected, self.bucket_repo.get_bucket(self.CUSTOMER_ID).items)

        with self.assertRaises(DoesNotExistItemError):
            self.order_service.add_items_to_bucket(self.CUSTOMER_ID, [Stock(0, 12)])


