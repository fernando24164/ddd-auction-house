from unittest import TestCase

from domain.money import Money


class TestMoney(TestCase):
    def test_greater_money(self):
        m = Money(123.3)
        m2 = Money(13.3)
        self.assertTrue(m > m2)

    def test_greater_equal_money(self):
        m = Money(123.3)
        m2 = Money(13.3)
        self.assertTrue(m >= m2)

    def test_less_equal_money(self):
        m = Money(1.3)
        m2 = Money(13.3)
        self.assertTrue(m <= m2)

    def test_less__money(self):
        m = Money(1.3)
        m2 = Money(13.3)
        self.assertTrue(m < m2)

    def test_eq_money(self):
        m = Money(123.3)
        m2 = Money(123.3)
        self.assertTrue(m == m2)

    def test_eq_money_diff_currency(self):
        m = Money(123.3)
        m2 = Money(123.3, currency="$")
        self.assertFalse(m == m2)
