import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"

    def test_home(self):
        response = requests.get(self.BASE_URL + "/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_recommend_valid(self):
        response = requests.get(self.BASE_URL + "/recommend?customer_id=12345")
        self.assertEqual(response.status_code, 200)

    def test_recommend_invalid(self):
        response = requests.get(self.BASE_URL + "/recommend?customer_id=99999")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
