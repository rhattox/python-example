import unittest

from main import app


class TestRegisterRoute(unittest.TestCase):

    def setUp(self):
        # Create a new Flask test client for each test method
        self.client = app.test_client()

    def test_register_success(self):
        # Test a successful registration
        response = self.client.post('/register', json={
            'name': 'testuser',
            'email': 'test@email.com',
            'password': 'testpassword'
        })

        print(response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
