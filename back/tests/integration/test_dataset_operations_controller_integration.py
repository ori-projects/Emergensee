import unittest
from fastapi.testclient import TestClient
from app.controllers.dataset_operations_controller import DatasetOperationsController
from app.entities.requests.risk_assessment_request import RiskAssessmentRequest

class TestDatasetOperationsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(DatasetOperationsController.get_app())

    def test_preprocess_datasets_integration(self):
        response = self.client.post("/preprocess_datasets")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_process_datasets_integration(self):
        response = self.client.post("/process_datasets")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_get_risk_assessment_integration(self):
        # Create a sample RiskAssessmentRequest object
        sample_request = {
            "some_field": "some_value"  # Replace with actual fields as required by RiskAssessmentRequest
        }
        response = self.client.post("/get-risk-assessment", json=sample_request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
