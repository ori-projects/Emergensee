import unittest
from fastapi.testclient import TestClient
from app.controllers.doctors_controller import DoctorsController

class TestDoctorsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(DoctorsController.get_app())

    def test_create_doctor_integration(self):
        response = self.client.post("/create-doctor", json={
            "user_id": 1,
            "rank": "Senior",
            "phoneNumber": "1234567890",
            "numberOfPatients": 50,
            "active": True,
            "dateOfBirth": "1980-01-01"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Doctor created successfully")

    def test_get_doctor_by_user_id_integration(self):
        # Assuming there is a doctor with user ID 1 for this test
        response = self.client.get("/get-doctor/1")
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
            self.assertIn("user_id", response.json())
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_doctor_integration(self):
        # Assuming there is a doctor with user ID 1 for this test
        response = self.client.put("/update-doctor/1", json={
            "rank": "Junior",
            "phoneNumber": "0987654321",
            "numberOfPatients": 30,
            "active": False,
            "dateOfBirth": "1985-05-05"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Doctor updated successfully")

    def test_delete_doctor_integration(self):
        # Assuming there is a doctor with user ID 1 for this test
        response = self.client.delete("/delete-doctor/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Doctor deleted successfully")

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
