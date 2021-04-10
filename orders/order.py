import uuid
from dataclasses import dataclass, field
from datetime import datetime

from orders.bucket import Bucket


@dataclass
class Order:
    customer_id: int
    bucket: Bucket
    cost: int
    created_date: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)
