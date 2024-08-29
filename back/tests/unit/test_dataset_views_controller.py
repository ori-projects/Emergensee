import unittest
from fastapi.testclient import TestClient
from app.controllers.dataset_views_controller import DatasetViewsController
from app.dal.proxy import Proxy

class TestDatasetViewsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(DatasetViewsController.get_app())
        self.proxy_instance = Proxy()
        self.ds_db_instance = self.proxy_instance.dataset_db

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_create_dataset(self):
        response = self.client.post("/create-dataset", json={
            "name": "Test Dataset",
            "description": "A test dataset for unit testing"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Dataset created successfully")

    def test_get_dataset(self):
        # First, create a dummy dataset to get its ID for testing
        create_response = self.client.post("/create-dataset", json={
            "name": "Test Dataset",
            "description": "A test dataset for unit testing"
        })
        self.assertEqual(create_response.status_code, 200)
        dataset_id = create_response.json().get("dataset_id")

        # Now test retrieving the dataset by ID
        response = self.client.get(f"/get-dataset/{dataset_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Test Dataset")

    def test_update_dataset_description(self):
        # First, create a dummy dataset to update its description
        create_response = self.client.post("/create-dataset", json={
            "name": "Test Dataset",
            "description": "A test dataset for unit testing"
        })
        self.assertEqual(create_response.status_code, 200)
        dataset_id = create_response.json().get("dataset_id")

        # Now update the dataset description
        update_response = self.client.put(f"/update-dataset-description/{dataset_id}", json={
            "new_description": "Updated description for testing"
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["message"], "Dataset description updated successfully")

    def test_delete_dataset(self):
        # First, create a dummy dataset to delete
        create_response = self.client.post("/create-dataset", json={
            "name": "Test Dataset",
            "description": "A test dataset for unit testing"
        })
        self.assertEqual(create_response.status_code, 200)
        dataset_id = create_response.json().get("dataset_id")

        # Now delete the dataset
        delete_response = self.client.delete(f"/delete-dataset/{dataset_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["message"], "Dataset deleted successfully")

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
