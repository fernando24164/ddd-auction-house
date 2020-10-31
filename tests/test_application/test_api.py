from application import create_app
from unittest import TestCase

from application.wsgi import app


class TestDevelopmentConfig(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app
        cls.client = create_app("test").test_client()

    def test_app_is_development(self):
        self.assertFalse(self.app.config["SECRET_KEY"] is "my_precious")
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertFalse(self.app is None)

    def test_app_response(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
