import unittest
from fastapi.testclient import TestClient
from app.controllers.models_controller import ModelsController

class TestModelsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(ModelsController.get_app())

    def test_create_model_integration(self):
        response = self.client.post("/create-model", json={
            "name": "TestModel",
            "labeled": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Model created successfully")

    def test_get_model_by_id_integration(self):
        # Assuming there is a model with ID 1 for this test
        response = self.client.get("/get-model/1")
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
            self.assertIn("name", response.json())
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_model_integration(self):
        # Assuming there is a model with ID 1 for this test
        response = self.client.put("/update-model/1", json={
            "name": "UpdatedModel",
            "labeled": False
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Model updated successfully")

    def test_delete_model_integration(self):
        # Assuming there is a model with ID 1 for this test
        response = self.client.delete("/delete-model/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Model deleted successfully")

    def test_get_all_models_integration(self):
        response = self.client.get("/get-all-models")
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json(), list)
        else:
            self.assertEqual(response.status_code, 404)

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
