from dataclasses import dataclass


@dataclass(eq=True)
class Coffee:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
