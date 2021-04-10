from orders.bucket import Bucket
from orders.bucketRepository import BucketRepository
from orders.orderRepository import OrderRepository, DoesNotExistOrderError
from orders.orderService import Choice
from tests.baseTest import BaseTest


class TestOrderRepository(BaseTest):
    CUSTOMER_ID = 1

    def setUp(self):
        super(TestOrderRepository, self).setUp()
        bucket = Bucket()
        bucket.put(Choice(self.latte.id, 1))

        self.bucket_repo = BucketRepository()
        self.bucket_repo.update_bucket(self.CUSTOMER_ID, bucket)

        self.order_repo = OrderRepository()

    def test_create(self):
        bucket = self.bucket_repo.get_bucket(self.CUSTOMER_ID)
        cost = bucket.get_cost(self.menu)
        order_id = self.order_repo.create(self.CUSTOMER_ID, bucket, cost)

        result = self.order_repo.get_order(order_id)
        self.assertEqual(self.CUSTOMER_ID, result.customer_id)
        self.assertEqual(bucket, result.bucket)
        self.assertEqual(cost, result.cost)

        with self.assertRaises(DoesNotExistOrderError):
            self.assertEqual(self.order_repo.get_order(-1))
