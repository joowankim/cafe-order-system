from orders.bucket import Bucket
from orders.bucketRepository import BucketRepository
from orders.orderService import Choice
from tests.baseTest import BaseTest


class TestBucketRepository(BaseTest):
    CUSTOMER_ID = 1

    def test_put(self):
        bucket = Bucket()
        bucket.put(Choice(self.latte.id, 1))

        bucket_repo = BucketRepository()
        bucket_repo.update_bucket(self.CUSTOMER_ID, bucket)
        expected = {
            self.CUSTOMER_ID: bucket
        }
        self.assertEqual(expected, bucket_repo.buckets)

    def test_get_bucket(self):
        bucket = Bucket()
        bucket.put(Choice(self.latte.id, 1))

        bucket_repo = BucketRepository()
        bucket_repo.update_bucket(self.CUSTOMER_ID, bucket)

        expected = bucket
        self.assertEqual(expected, bucket_repo.get_bucket(self.CUSTOMER_ID))

        # check empty bucket
        self.assertEqual({}, bucket_repo.get_bucket(2))
