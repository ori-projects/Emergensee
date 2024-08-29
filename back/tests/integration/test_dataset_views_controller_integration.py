import unittest
from fastapi.testclient import TestClient
from app.controllers.dataset_views_controller import DatasetViewsController

class TestDatasetViewsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(DatasetViewsController.get_app())

    def test_create_dataset_integration(self):
        response = self.client.post("/create-dataset", json={
            "name": "Test Dataset",
            "description": "A description for the test dataset"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Dataset created successfully")

    def test_get_dataset_integration(self):
        # Assuming there is a dataset with ID 1 for this test
        response = self.client.get("/get-dataset/1")
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
            self.assertIn("name", response.json())
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_dataset_description_integration(self):
        # Assuming there is a dataset with ID 1 for this test
        response = self.client.put("/update-dataset-description/1", json={
            "new_description": "Updated description for the dataset"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Dataset description updated successfully")

    def test_delete_dataset_integration(self):
        # Assuming there is a dataset with ID 1 for this test
        response = self.client.delete("/delete-dataset/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Dataset deleted successfully")

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
