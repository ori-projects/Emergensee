import unittest
from fastapi.testclient import TestClient
from app.controllers.tools_controller import ToolsController
from app.entities.datasets.disease import Disease
from app.entities.datasets.ckd import Ckd
from app.entities.datasets.cassi import Cassi
from app.entities.datasets.maternal import Maternal

class TestToolsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(ToolsController.get_app())

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_test_cass_controller(self):
        response = self.client.post("/test-cass")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Done")

    def test_test_maternal_controller(self):
        response = self.client.post("/test-maternal")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Done")

    def test_test_ckd_controller(self):
        response = self.client.post("/test-ckd")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Done")

    def test_test_disease_controller(self):
        response = self.client.post("/test-disease")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Done")

    def test_make_test_files_controller(self):
        response = self.client.post("/make-test-files")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Done")

    def test_test_files_controller(self):
        response = self.client.post("/test-files")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Done")

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
