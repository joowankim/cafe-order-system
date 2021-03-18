from dataclasses import dataclass


@dataclass
class Receipt:
    customer_name: str
    seller_name: str
    product: str
    price: int
    amount: int
    ordered_date: str
