import unittest
from fastapi.testclient import TestClient
from fastapi import FastAPI
import json

import os, sys
sys.path.insert(0, os.path.abspath('..'))
import sql_app.main as main
import sql_app.crud as crud
import sql_app.models as models
import sql_app.schemas as schemas


app = main.app
client = TestClient(app)

class test_main(unittest.TestCase):
    def reset_test_database(self):
        response = client.get("/test/")
        self.assertTrue(response.status_code == 200)

    def test_read_users(self):
        """This unit test mesures the expected json and expected response against those received.
        """

        self.reset_test_database()

        expected_json = json.loads("""[{"email": "tieg@gmail.com", "id": 1, "is_active": true, "items": [{"title": "tiegs pencil", 
        "description": "here lies tieg pencil", "id": 1, "owner_id": 1}, {"title": "tiegs pencil", 
        "description": "tiegs backup pencil", "id": 2, "owner_id": 1}]}, {"email": "troy@gmail.com", 
        "id": 2, "is_active": false, "items": [{"title": "troys bag", "description": "this is troys bag", 
        "id": 3, "owner_id": 2}]}]""")
        expected_response = 200

        response = client.get("/users/")
        self.assertTrue(response.status_code == expected_response)
        self.assertTrue(response.json() == expected_json)
    
    def test_read_user(self):
        expected_json = json.loads("""{"email": "tieg@gmail.com", "id": 1, "is_active": true, "items": [{"title": "tiegs pencil", 
        "description": "here lies tieg pencil", "id": 1, "owner_id": 1}, {"title": "tiegs pencil", 
        "description": "tiegs backup pencil", "id": 2, "owner_id": 1}]}""")
        expected_response = 200

        response = client.get("/users/1")
        self.assertTrue(response.status_code == expected_response)
        self.assertTrue(response.json() == expected_json)

    def test_read_items(self):
        expected_json = json.loads("""[{"title": "tiegs pencil", "description": "here lies tieg pencil", "id": 1, "owner_id": 1}, 
        {"title": "tiegs pencil", "description": "tiegs backup pencil", "id": 2, "owner_id": 1}, {"title": "troys bag", 
        "description": "this is troys bag", "id": 3, "owner_id": 2}]""")
        expected_response = 200

        response = client.get("/items/")
        self.assertTrue(response.status_code == expected_response)
        # print(str(response.json()).replace('\'', '\"').replace('True', 'true').replace('False', 'false'))
        self.assertTrue(response.json() == expected_json)