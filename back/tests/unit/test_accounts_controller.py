import unittest
from fastapi.testclient import TestClient
from app.controllers.accounts_controller import AccountsController

class TestAccountsController(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(AccountsController.get_app())

    def test_get_accounts(self):
        response = self.client.get("/get-accounts")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()