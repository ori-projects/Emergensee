import unittest
from fastapi.testclient import TestClient
from app.controllers.admins_controller import AdminsController

class TestAdminsControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(AdminsController.get_app())

    def test_create_admin_integration(self):
        response = self.client.post("/create-admin", json={"user_id": 123})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Admin created successfully")

    def test_get_admin_by_user_id_integration(self):
        response = self.client.get("/get-admin/123")
        self.assertEqual(response.status_code, 200)

    def test_delete_admin_integration(self):
        response = self.client.delete("/delete-admin/123")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Admin deleted successfully")

    def test_health_check_integration(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()