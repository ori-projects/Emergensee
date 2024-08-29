import unittest
from fastapi.testclient import TestClient
from app.controllers.utils_controller import UtilsController

class TestUtilsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(UtilsController.get_app())

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_get_enums_controller(self):
        response = self.client.get("/get-enums")
        self.assertEqual(response.status_code, 200)
        self.assertIn("enums", response.json())
        selected_enums = response.json()["enums"]
        self.assertIn("Operative_Procedure", selected_enums)
        self.assertIn("Feelings_and_Urge", selected_enums)
        self.assertIn("Disease", selected_enums)
        self.assertIn("Critical_Feelings", selected_enums)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
