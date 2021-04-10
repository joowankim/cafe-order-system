from orders.bucket import Bucket, NegativeIntegerError
from orders.orderService import Choice
from tests.baseTest import BaseTest


class TestBucket(BaseTest):
    def test_put(self):
        bucket = Bucket()
        bucket.put(Choice(self.latte.id, 1))
        self.assertEqual(1, bucket.items[self.latte.id])
        with self.assertRaises(NegativeIntegerError):
            bucket.put(Choice(self.latte.id, -1))

    def test_get_item(self):
        bucket = Bucket()
        bucket.put(Choice(self.latte.id, 1))
        self.assertEqual(1, bucket.get_item(self.latte.id))
        self.assertEqual(0, bucket.get_item(self.americano.id))
