from dataclasses import dataclass, field
from typing import AnyStr, Iterator
from uuid import uuid4

from domain.item import Item
from domain.money import Money
from domain.exceptions import NotFoundException


@dataclass
class User:
    name: AnyStr
    user_id: AnyStr = field(default_factory=uuid4)
    items: Item = field(default_factory=list)

    def add_item(
        self, quantity: int, name: AnyStr, description: AnyStr, price: Money
    ) -> None:
        self.items.append(Item(quantity, name, description, price))

    def remove_item(self, item_id) -> bool:
        """Remove item with a item_id given

        :param item_id:
        :type item_id: str
        :raises NotFoundException: if not item deleted will raise an exception
        :return: True if element got deleted
        :rtype: bool
        """
        for index, item in enumerate(self.items):
            if item.item_id == item_id:
                if item.quantity > 1:
                    item.quantity -= 1
                else:
                    del self.items[index]
                return True
        raise NotFoundException

    def list_items(self) -> Iterator[Item]:
        for item in self.items():
            yield item
