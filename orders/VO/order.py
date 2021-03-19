from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    customer_info: str
    product: str
    amount: int
    price: int
    ordered: str
