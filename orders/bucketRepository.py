from collections import defaultdict

from orders.bucket import Bucket


class BucketRepository:
    def __init__(self):
        self.buckets = defaultdict(Bucket)

    def update_bucket(self, customer_id, bucket):
        self.buckets[customer_id] = bucket

    def get_bucket(self, customer_id):
        return self.buckets.get(customer_id, {})
