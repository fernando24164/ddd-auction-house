from dataclasses import dataclass

from domain.money import Money
from domain.user import User


@dataclass
class Bid:
    money: Money
    player: User

    def __gt__(self, value):
        return self.money > value.money

    def __ge__(self, value):
        return self.money >= value.money

    def __le__(self, value):
        return self.money <= value.money

    def __lt__(self, value):
        return self.money < value.money
