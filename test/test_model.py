import unittest
import requests


class TestModel(unittest.TestCase):
    def test_main(self):
        print("test main : START")
        pass

    def test_coin_model(self):
        print("\n test coin model : START")
        self.assertEqual(True, True)

    def test_request(self):
        response = requests.get("http://api.open-notify.org/astros.json")
        print(response.json())