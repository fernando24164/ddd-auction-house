from unittest import TestCase

from domain.user import User
from domain.item import Item
from domain.auction import Auction
from domain.money import Money
from infrastructure.fake_auction import FakeAuctionRepository
from infrastructure.fake_user import FakeUserRepository
from infrastructure.exceptions import NotFoundException


class FakeRepositoryTests(TestCase):
    def setUp(self):
        self.auction = Auction(
            creator=User("test_user"),
            items=[
                Item(1, "test_item", "test", Money(12.0)),
                Item(1, "test_item", "test", Money(12.0)),
            ],
        )
        self.repository = FakeAuctionRepository()
        self.repository.add(self.auction)

    def test_add_new_auction(self):
        self.repository.add(self.auction)
        self.assertEqual(len(self.repository.auctions), 2)

    def test_get_auction(self):
        stored_auction = self.repository.get(self.auction.auction_id)
        self.assertEqual(
            stored_auction.auction_id,
            self.repository.get(self.auction.auction_id).auction_id,
        )

    def test_update_auction(self):
        self.repository.update(
            self.auction.auction_id,
            {
                "items": [
                    Item(1, "test_item", "test", Money(12.0)),
                    Item(1, "test_item", "test", Money(12.0)),
                ]
            },
        )
        self.assertNotEqual(
            self.auction.items,
            [
                Item(1, "test_item", "test", Money(12.0)),
                Item(1, "test_item", "test", Money(11.0)),
            ],
        )

    def test_list_auction(self):
        list_auction = list(self.repository.list_all())
        self.assertIsInstance(list_auction, list)

    def test_delete_auction(self):
        try:
            self.repository.delete(self.auction.auction_id)
        except NotFoundException:
            pass
        list_auction = list(self.repository.list_all())
        self.assertEqual(len(list_auction), 0)


class FakeRepositoryUserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User(name="Test-user")
        cls.user.add_item(1, "Spectrum", "Vintage home computer system", Money(300.50))
        cls.user.add_item(2, "Amiga", "Older computer", Money(50.49))
        cls.repository = FakeUserRepository()

    def test_add_new_user(self):
        self.repository.add(self.user)
        self.assertEqual(len(self.repository.users), 1)

    def test_get_user(self):
        self.repository.add(self.user)
        stored_user = self.repository.get(self.user.user_id)
        self.assertEqual(
            stored_user.user_id, self.repository.get(self.user.user_id).user_id
        )

    def test_list_users(self):
        self.repository.add(self.user)
        list_user = list(self.repository.list_all())
        self.assertIsInstance(list_user, list)

    def test_delete_user(self):
        self.repository.add(self.user)
        try:
            self.repository.delete(self.user.user_id)
        except NotFoundException:
            pass
        list_user = list(self.repository.list_all())
        self.assertEqual(len(list_user), 0)
