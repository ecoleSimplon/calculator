from os import pardir
import unittest
from unittest import result
import requests


class ApiResponse(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ApiResponse, self).__init__(*args, **kwargs)
        self.url_addition = "http://localhost:5000/addition"
        self.url_multiplication = "http://localhost:5000/multiplication"
        self.url_division = "http://localhost:5000/division"
        self.url_subtraction = "http://localhost:5000/subtraction"

    def test_status_code(self):
            payload = {"a": 1, "b": 2}

            response_addition = requests.get(self.url_addition, params=payload)
            response_multiplication = requests.get(self.url_multiplication, params=payload)
            response_division = requests.get(self.url_division, params=payload)
            response_subtraction = requests.get(self.url_subtraction, params=payload)

            self.assertEqual(response_addition.status_code, 200)
            self.assertEqual(response_multiplication.status_code, 200)
            self.assertEqual(response_division.status_code, 200)
            self.assertEqual(response_subtraction.status_code, 200)

       

    def test_operation_result(self):
        payload = {"a": 1, "b": 0}

        response_addition = requests.get(self.url_addition, params=payload)
        response_multiplication = requests.get(self.url_multiplication, params=payload)
        response_division = requests.get(self.url_division, params=payload)
        response_subtraction = requests.get(self.url_subtraction, params=payload)
        
        result_addition = response_addition.json()
        result_multiplication = response_multiplication.json()
        result_division = response_division.json()
        result_subtraction = response_subtraction.json()

        self.assertEqual(result_addition, 1)
        self.assertEqual(result_multiplication, 0)
        self.assertEqual(result_division, "float division by zero")
        self.assertEqual(result_subtraction, 1)

        payload = {"a": 1, "b": "z"}
        response_addition = requests.get(self.url_addition, params=payload)
        result_addition = response_addition.json()
        self.assertEqual(result_addition, "could not convert string to float: 'z'")

    

if __name__ == '__main__':
    unittest.main()