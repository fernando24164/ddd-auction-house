from dataclasses import dataclass, field
from typing import AnyStr


@dataclass()
class Money:
    quantity: float
    currency: AnyStr = "€"

    def __gt__(self, value):
        return self.quantity > value.quantity

    def __ge__(self, value):
        return self.quantity >= value.quantity

    def __lt__(self, value):
        return self.quantity < value.quantity

    def __le__(self, value):
        return self.quantity <= value.quantity
