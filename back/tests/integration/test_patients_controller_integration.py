import unittest
from fastapi.testclient import TestClient
from app.controllers.patients_controller import PatientsController

class TestPatientsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(PatientsController.get_app())

    def test_create_patient_integration(self):
        response = self.client.post("/create-patient", json={
            "name": "John Doe",
            "description": "Test patient",
            "imagePath": "/path/to/image",
            "email": "john.doe@example.com",
            "doctor_id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Patient created successfully")

    def test_get_patients_by_doctor_id_integration(self):
        # Assuming there is a doctor with ID 1 and patients associated with this doctor
        response = self.client.get("/get-patients/1")
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json(), list)
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_patient_integration(self):
        # Assuming there is a patient with ID 1 for this test
        response = self.client.put("/update-patient/1", json={
            "name": "Jane Doe",
            "description": "Updated test patient",
            "imagePath": "/new/path/to/image",
            "email": "jane.doe@example.com",
            "doctor_id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Patient updated successfully")

    def test_delete_patient_integration(self):
        # Assuming there is a patient with ID 1 for this test
        response = self.client.delete("/delete-patient/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Patient deleted successfully")

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
