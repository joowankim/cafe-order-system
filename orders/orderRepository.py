from orders.order import Order


class DoesNotExistOrderError(ValueError):
    def __init__(self, value):
        super(DoesNotExistOrderError, self).__init__(f"order {value} does not exist")


class OrderRepository:
    def __init__(self):
        self.orders = dict()

    def create(self, customer_id, bucket, cost):
        order = Order(
            customer_id=customer_id,
            bucket=bucket,
            cost=cost
        )
        self.orders[order.id] = order
        return order.id

    def get_order(self, order_id):
        try:
            return self.orders[order_id] 
        except KeyError:
            raise DoesNotExistOrderError(order_id)
