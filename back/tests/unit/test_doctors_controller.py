import unittest
from fastapi.testclient import TestClient
from app.controllers.doctors_controller import DoctorsController
from app.dal.proxy import Proxy

class TestDoctorsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(DoctorsController.get_app())
        self.proxy_instance = Proxy()
        self.account_db_instance = self.proxy_instance.account_db

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_create_doctor(self):
        response = self.client.post("/create-doctor", json={
            "user_id": 123,
            "rank": "Senior Doctor",
            "phoneNumber": "+1234567890",
            "numberOfPatients": 50,
            "active": True,
            "dateOfBirth": "1980-01-01"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Doctor created successfully")

    def test_get_doctor_by_user_id(self):
        # First, create a dummy doctor to get its ID for testing
        create_response = self.client.post("/create-doctor", json={
            "user_id": 123,
            "rank": "Junior Doctor",
            "phoneNumber": "+9876543210",
            "numberOfPatients": 30,
            "active": True,
            "dateOfBirth": "1990-01-01"
        })
        self.assertEqual(create_response.status_code, 200)
        user_id = create_response.json().get("user_id")

        # Now test retrieving the doctor by user ID
        response = self.client.get(f"/get-doctor/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["rank"], "Junior Doctor")

    def test_update_doctor(self):
        # First, create a dummy doctor to update its details
        create_response = self.client.post("/create-doctor", json={
            "user_id": 123,
            "rank": "Junior Doctor",
            "phoneNumber": "+9876543210",
            "numberOfPatients": 30,
            "active": True,
            "dateOfBirth": "1990-01-01"
        })
        self.assertEqual(create_response.status_code, 200)
        user_id = create_response.json().get("user_id")

        # Now update the doctor details
        update_response = self.client.put(f"/update-doctor/{user_id}", json={
            "rank": "Senior Doctor",
            "phoneNumber": "+1234567890",
            "numberOfPatients": 50,
            "active": True,
            "dateOfBirth": "1980-01-01"
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["message"], "Doctor updated successfully")

    def test_delete_doctor(self):
        # First, create a dummy doctor to delete
        create_response = self.client.post("/create-doctor", json={
            "user_id": 123,
            "rank": "Junior Doctor",
            "phoneNumber": "+9876543210",
            "numberOfPatients": 30,
            "active": True,
            "dateOfBirth": "1990-01-01"
        })
        self.assertEqual(create_response.status_code, 200)
        user_id = create_response.json().get("user_id")

        # Now delete the doctor
        delete_response = self.client.delete(f"/delete-doctor/{user_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["message"], "Doctor deleted successfully")

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
