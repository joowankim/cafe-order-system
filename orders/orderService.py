from collections import namedtuple
from typing import List

from orders.bucketRepository import BucketRepository
from orders.coffeeRepository import CoffeeRepository
from orders.menu import Menu
from orders.orderRepository import OrderRepository

Choice = namedtuple(typename='Choice', field_names=['id', 'count'])


class ExceedOnHandError(OverflowError):
    def __init__(self, value):
        super(ExceedOnHandError, self).__init__(f"Amount of {value} exceed holding amount")


class OrderService:
    def __init__(self,
                 coffee_repo: CoffeeRepository,
                 bucket_repo: BucketRepository,
                 order_repo: OrderRepository,
                 menu: Menu):
        self.coffee_repo = coffee_repo
        self.bucket_repo = bucket_repo
        self.order_repo = order_repo
        self.menu = menu

    def get_menu(self):
        """
        get all of items list in menu

        :return: list of products and amount
        """
        inventory = self.coffee_repo.get_inventory()
        items = self.menu.get_items()
        return [{'id': item.id,
                 'name': item.name,
                 'price': item.price,
                 'amount': inventory.get(item.id, 0)}
                for item in items]

    def add_items_to_bucket(self, customer_id, choices: List[Choice]):
        bucket = self.bucket_repo.get_bucket(customer_id)
        inventory = self.coffee_repo.get_inventory()

        exceeded_items = []
        for item in choices:
            if bucket.get_item(item.id) + item.count > inventory.get(item.id, 0):
                exceeded_items.append(self.menu.get_item_name(item.id))
        if exceeded_items:
            raise ExceedOnHandError(', '.join(exceeded_items))

        for item in choices:
            bucket.put(item)
        return self.bucket_repo.get_bucket(customer_id)

    def create_order(self, customer_id, bucket):
        cost = bucket.get_cost(self.menu)
        order_id = self.order_repo.create(customer_id, bucket, cost)
        return self.order_repo.get_order(order_id)
