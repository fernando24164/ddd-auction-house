from unittest import TestCase

from domain.user import User
from domain.money import Money
from domain.exceptions import NotFoundException


class TestUser(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User("global_user")
        cls.user.add_item(2, "Amiga", "older computer", Money(112.20))

    def test_user_creation(self):
        test_user = User("test_user")
        self.assertIsInstance(test_user, User)

    def test_user_delete_item(self):
        try:
            self.user.remove_item(self.user.items[0].item_id)
        except NotFoundException:
            self.fail("Raised not found exception unexpectedly")

    def test_user_delete_item_exception(self):
        with self.assertRaises(NotFoundException) as context:
            self.user.remove_item("1")
            self.assertTrue('NotFoundException' in context.exception)
