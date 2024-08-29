import unittest
from fastapi.testclient import TestClient
from app.controllers.tools_controller import ToolsController

class TestToolsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(ToolsController.get_app())

    def test_test_cass_controller_integration(self):
        response = self.client.post("/test-cass")
        self.assertEqual(response.status_code, 200)

    def test_test_maternal_controller_integration(self):
        response = self.client.post("/test-maternal")
        self.assertEqual(response.status_code, 200)

    def test_test_ckd_controller_integration(self):
        response = self.client.post("/test-ckd")
        self.assertEqual(response.status_code, 200)

    def test_test_disease_controller_integration(self):
        response = self.client.post("/test-disease")
        self.assertEqual(response.status_code, 200)

    def test_get_test_files_integration(self):
        response = self.client.post("/make-test-files")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Done")

    def test_test_files_integration(self):
        response = self.client.post("/test-files")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Done")

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
