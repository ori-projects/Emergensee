import unittest
from fastapi.testclient import TestClient
from app.controllers.widgets_controller import WidgetsController

class TestWidgetsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(WidgetsController.get_app())

    def test_get_widgets_integration(self):
        response = self.client.get("/get-widgets")
        self.assertIn(response.status_code, [200, 404])
        if response.status_code == 200:
            self.assertIsInstance(response.json(), list)
        elif response.status_code == 404:
            self.assertEqual(response.json()["detail"], "Widgets not found")

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()