import unittest
from fastapi.testclient import TestClient
from app.controllers.models_controller import ModelsController
from app.dal.proxy import Proxy

class TestModelsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(ModelsController.get_app())
        self.proxy_instance = Proxy()
        self.models_db_instance = self.proxy_instance.model_db

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_create_model(self):
        response = self.client.post("/create-model", json={
            "name": "Model A",
            "labeled": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Model created successfully")

    def test_get_model_by_id(self):
        # First, create a dummy model to get its ID for testing
        create_response = self.client.post("/create-model", json={
            "name": "Model B",
            "labeled": False
        })
        self.assertEqual(create_response.status_code, 200)
        model_id = create_response.json().get("model_id")

        # Now test retrieving the model by ID
        response = self.client.get(f"/get-model/{model_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Model B")

    def test_update_model(self):
        # First, create a dummy model to update its details
        create_response = self.client.post("/create-model", json={
            "name": "Model C",
            "labeled": True
        })
        self.assertEqual(create_response.status_code, 200)
        model_id = create_response.json().get("model_id")

        # Now update the model details
        update_response = self.client.put(f"/update-model/{model_id}", json={
            "name": "Model D",
            "labeled": False
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["message"], "Model updated successfully")

    def test_delete_model(self):
        # First, create a dummy model to delete
        create_response = self.client.post("/create-model", json={
            "name": "Model E",
            "labeled": True
        })
        self.assertEqual(create_response.status_code, 200)
        model_id = create_response.json().get("model_id")

        # Now delete the model
        delete_response = self.client.delete(f"/delete-model/{model_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["message"], "Model deleted successfully")

    def test_get_all_models(self):
        # First, create some dummy models to ensure there are models to retrieve
        self.client.post("/create-model", json={
            "name": "Model F",
            "labeled": True
        })
        self.client.post("/create-model", json={
            "name": "Model G",
            "labeled": False
        })

        # Now test retrieving all models
        response = self.client.get("/get-all-models")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
