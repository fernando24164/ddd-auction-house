from unittest import TestCase

from domain.auction import Auction
from domain.user import User
from domain.item import Item
from domain.money import Money
from domain.bid import Bid


class TestAuction(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = User(name="Test_User")
        cls.user.add_item(1, "Spectrum", "Vintage home computer system", Money(300.50))
        cls.user.add_item(2, "Amiga", "Older computer", Money(50.49))

        cls.user2 = User(name="Test_User2")
        cls.user2.add_item(1, "Spectrum", "Vintage home computer system", Money(300.50))
        cls.user2.add_item(2, "Amiga", "Older computer", Money(50.49))

    def test_auction_creation(self):
        auction_test = Auction(creator=self.user, items=[self.user.items[0]])
        auction_test2 = Auction(creator=self.user2, items=[self.user.items[0]])
        self.assertIsNotNone(auction_test)
        self.assertNotEqual(auction_test.items, auction_test2.items)
        self.assertNotEqual(auction_test.due_date, auction_test2.due_date)

    def test_update_auction(self):
        auction_test = Auction(creator=self.user, items=[self.user.items[0]])
        item_to_update = self.user.items[0]
        auction_test.update_auction(params={"items": [item_to_update]})
        self.assertEqual(auction_test.items, [item_to_update])

    def test_make_bid(self):
        auction_test = Auction(creator=self.user, items=[self.user.items[0]])
        auction_test.make_bid(Bid(Money(23.0), self.user2))
        self.assertGreater(len(auction_test.bids), 0)

    def test_make_incorrect_bid(self):
        auction_test = Auction(creator=self.user, items=[self.user.items[0]])
        self.assertFalse(auction_test.make_bid(Bid(Money(23.0), self.user)))
