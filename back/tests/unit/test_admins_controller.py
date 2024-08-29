import unittest
from fastapi.testclient import TestClient
from app.controllers.admins_controller import AdminsController

class TestAdminsController(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(AdminsController.get_app())

    def test_create_admin(self):
        response = self.client.post("/create-admin", json={"user_id": 123})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Admin created successfully")

    def test_get_admin_by_user_id(self):
        response = self.client.get("/get-admin/123")
        self.assertEqual(response.status_code, 200)

    def test_delete_admin(self):
        response = self.client.delete("/delete-admin/123")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Admin deleted successfully")

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()