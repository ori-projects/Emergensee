import unittest
from fastapi.testclient import TestClient
from app.controllers.widgets_controller import WidgetsController

class TestWidgetsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(WidgetsController.get_app())

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_get_widgets(self):
        response = self.client.get("/get-widgets")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()