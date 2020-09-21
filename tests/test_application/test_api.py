from unittest import TestCase

from application.wsgi import app


class TestDevelopmentConfig(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app

    def test_app_is_development(self):
        self.assertFalse(self.app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(self.app is None)
