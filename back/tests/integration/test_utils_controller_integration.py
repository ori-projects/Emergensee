import unittest
from fastapi.testclient import TestClient
from app.controllers.utils_controller import UtilsController

class TestUtilsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(UtilsController.get_app())

    def test_get_enums_controller_integration(self):
        response = self.client.get("/get-enums")
        self.assertEqual(response.status_code, 200)
        self.assertIn("enums", response.json())
        self.assertIn("Operative_Procedure", response.json()["enums"])
        self.assertIn("Feelings_and_Urge", response.json()["enums"])
        self.assertIn("Disease", response.json()["enums"])
        self.assertIn("Critical_Feelings", response.json()["enums"])

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
