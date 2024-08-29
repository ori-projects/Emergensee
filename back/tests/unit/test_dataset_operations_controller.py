import unittest
from fastapi.testclient import TestClient
from app.controllers.dataset_operations_controller import DatasetOperationsController
from app.services.dataset_ops.dataset_operation_service import DatasetOperationService
from app.entities.requests.risk_assessment_request import RiskAssessmentRequest

class TestDatasetOperationsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(DatasetOperationsController.get_app())

    def test_preprocess_datasets(self):
        response = self.client.post("/preprocess_datasets")
        self.assertEqual(response.status_code, 200)
        self.assertIn("preprocessed", response.json()["message"])

    def test_process_datasets(self):
        response = self.client.post("/process_datasets")
        self.assertEqual(response.status_code, 200)
        self.assertIn("processed", response.json()["message"])

    def test_get_risk_assessment(self):
        # Create a sample RiskAssessmentRequest object
        data = RiskAssessmentRequest(...)
        response = self.client.post("/get-risk-assessment", json=data.dict())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Details of risk assessment calculations:", response.json()["message"])

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
