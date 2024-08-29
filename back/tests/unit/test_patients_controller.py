import unittest
from fastapi.testclient import TestClient
from app.controllers.patients_controller import PatientsController
from app.dal.proxy import Proxy

class TestPatientsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(PatientsController.get_app())
        self.proxy_instance = Proxy()
        self.account_db_instance = self.proxy_instance.account_db

    def tearDown(self):
        # Clean up any test data after each test if needed
        pass

    def test_create_patient(self):
        response = self.client.post("/create-patient", json={
            "name": "John Doe",
            "description": "Patient with condition X",
            "imagePath": "/path/to/image.jpg",
            "email": "john.doe@example.com",
            "doctor_id": 12345
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Patient created successfully")

    def test_get_patients_by_doctor_id(self):
        # First, create a dummy patient to associate with a doctor for testing
        create_response = self.client.post("/create-patient", json={
            "name": "Jane Smith",
            "description": "Patient with condition Y",
            "imagePath": "/path/to/image2.jpg",
            "email": "jane.smith@example.com",
            "doctor_id": 12345
        })
        self.assertEqual(create_response.status_code, 200)

        # Now test retrieving patients by doctor ID
        response = self.client.get("/get-patients/12345")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_update_patient(self):
        # First, create a dummy patient to update its details
        create_response = self.client.post("/create-patient", json={
            "name": "Emily Brown",
            "description": "Patient with condition Z",
            "imagePath": "/path/to/image3.jpg",
            "email": "emily.brown@example.com",
            "doctor_id": 54321
        })
        self.assertEqual(create_response.status_code, 200)
        patient_id = create_response.json().get("patient_id")

        # Now update the patient details
        update_response = self.client.put(f"/update-patient/{patient_id}", json={
            "name": "Emily Green",
            "description": "Patient with condition Z updated",
            "imagePath": "/path/to/image4.jpg",
            "email": "emily.green@example.com",
            "doctor_id": 54321
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["message"], "Patient updated successfully")

    def test_delete_patient(self):
        # First, create a dummy patient to delete
        create_response = self.client.post("/create-patient", json={
            "name": "Michael Johnson",
            "description": "Patient with condition W",
            "imagePath": "/path/to/image5.jpg",
            "email": "michael.johnson@example.com",
            "doctor_id": 54321
        })
        self.assertEqual(create_response.status_code, 200)
        patient_id = create_response.json().get("patient_id")

        # Now delete the patient
        delete_response = self.client.delete(f"/delete-patient/{patient_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["message"], "Patient deleted successfully")

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
