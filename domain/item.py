from dataclasses import dataclass, field
from uuid import uuid4
from typing import AnyStr

from domain.money import Money


@dataclass
class Item:
    quantity: int
    name: AnyStr
    description: AnyStr
    price: Money
    item_id: AnyStr = field(default_factory=uuid4)
