import unittest
from fastapi.testclient import TestClient
from app.controllers.algorithms_controller import AlgorithmsController

class TestAlgorithmsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(AlgorithmsController.get_app())

    def test_create_algorithm_integration(self):
        response = self.client.post("/create-algorithm", json={
            "algorithm_name": "Test Algorithm",
            "success_rank": 1,
            "num_uses": 10
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Algorithm created successfully")

    def test_get_algorithms_integration(self):
        response = self.client.get("/get-algorithms")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_algorithm_by_id_integration(self):
        # Assuming there is an algorithm with ID 1 for this test
        response = self.client.get("/get-algorithm/1")
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
            self.assertIn("algorithm_name", response.json())
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_algorithm_integration(self):
        # Assuming there is an algorithm with ID 1 for this test
        response = self.client.put("/update-algorithm/1", json={
            "algorithm_name": "Updated Algorithm",
            "success_rank": 2,
            "num_uses": 20
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Algorithm updated successfully")

    def test_delete_algorithm_integration(self):
        # Assuming there is an algorithm with ID 1 for this test
        response = self.client.delete("/delete-algorithm/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Algorithm deleted successfully")

    def test_get_algorithm_statistics_integration(self):
        response = self.client.get("/get-algorithm-statistics")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
