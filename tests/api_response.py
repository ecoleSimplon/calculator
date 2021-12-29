import unittest
import requests
import argparse


def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url", nargs="+")
    arg_url = parser.parse_args()
    return arg_url

class ApiResponse(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ApiResponse, self).__init__(*args, **kwargs)
        self.base_url = get_arg().url[0]
        self.url_addition = self.base_url + "/addition"
        self.url_multiplication = self.base_url + "/multiplication"
        self.url_division = self.base_url + "/division"
        self.url_subtraction = self.base_url + "/subtraction"


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
    arg = get_arg()
    unittest.main(argv=arg.url)