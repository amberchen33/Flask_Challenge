import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_get_prime_success(self):
        r = requests.get('http://localhost:5000/get_prime?start=2&end=10')
        self.assertEqual(r.status_code, 200)

    def test_get_prime_fail(self):
        r = requests.get('http://localhost:5000/get_prime')
        self.assertEqual(r.status_code, 500)
        self.assertEqual(r.text, 'error: not get start or end parameters')

if __name__ == '__main__':
    unittest.main()