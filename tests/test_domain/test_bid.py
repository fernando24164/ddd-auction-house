from unittest import TestCase

from domain.bid import Bid
from domain.user import User
from domain.money import Money


class TestBid(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User("test_user")

    def test_eq_bid(self):
        b = Bid(Money(1.1), self.user)
        b2 = Bid(Money(1.1), self.user)
        self.assertTrue(b == b2)

    def test_gt_bid(self):
        b = Bid(Money(1.2), self.user)
        b2 = Bid(Money(1.1), self.user)
        self.assertTrue(b > b2)

    def test_less_bid(self):
        b = Bid(Money(0.9), self.user)
        b2 = Bid(Money(1.1), self.user)
        self.assertTrue(b < b2)

