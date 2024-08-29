import unittest
from fastapi.testclient import TestClient
from app.controllers.algorithms_controller import AlgorithmsController

class TestAlgorithmsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(AlgorithmsController.get_app())

    def test_create_algorithm(self):
        response = self.client.post("/create-algorithm", json={
            "algorithm_name": "Test Algorithm",
            "success_rank": 5,
            "num_uses": 0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Algorithm created successfully")

    def test_get_algorithms(self):
        response = self.client.get("/get-algorithms")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_algorithm_by_id(self):
        # First, create a dummy algorithm to get its ID for testing
        create_response = self.client.post("/create-algorithm", json={
            "algorithm_name": "Test Algorithm",
            "success_rank": 5,
            "num_uses": 0
        })
        self.assertEqual(create_response.status_code, 200)
        algorithm_id = create_response.json().get("algorithm_id")

        # Now test retrieving the algorithm by ID
        response = self.client.get(f"/get-algorithm/{algorithm_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["algorithm_id"], algorithm_id)

    def test_update_algorithm(self):
        # First, create a dummy algorithm to update
        create_response = self.client.post("/create-algorithm", json={
            "algorithm_name": "Test Algorithm",
            "success_rank": 5,
            "num_uses": 0
        })
        self.assertEqual(create_response.status_code, 200)
        algorithm_id = create_response.json().get("algorithm_id")

        # Now update the algorithm
        update_response = self.client.put(f"/update-algorithm/{algorithm_id}", json={
            "algorithm_name": "Updated Algorithm",
            "success_rank": 7,
            "num_uses": 10
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["message"], "Algorithm updated successfully")

    def test_delete_algorithm(self):
        # First, create a dummy algorithm to delete
        create_response = self.client.post("/create-algorithm", json={
            "algorithm_name": "Test Algorithm",
            "success_rank": 5,
            "num_uses": 0
        })
        self.assertEqual(create_response.status_code, 200)
        algorithm_id = create_response.json().get("algorithm_id")

        # Now delete the algorithm
        delete_response = self.client.delete(f"/delete-algorithm/{algorithm_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["message"], "Algorithm deleted successfully")

    def test_get_algorithm_statistics(self):
        response = self.client.get("/get-algorithm-statistics")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
