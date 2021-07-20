import unittest
import requests
import os
import logging


class TestModel(unittest.TestCase):
    def test_main(self):
        print("Test main : START")
        pass

    def test_coin_model(self):
        print("Test coin model : START")
        self.assertEqual(True, True)

    def test_bnb_details(self):
        bnb_api_key = os.environ.get('BNB_API_KEY')
        bnb_api_sec = os.environ.get('BNB_SEC_KEY')
        self.assertIsNotNone(bnb_api_key)
        self.assertIsNotNone(bnb_api_sec)
        print(f"BNB API key : {bnb_api_key}")
        print(f"BNB API key : {bnb_api_sec}")
