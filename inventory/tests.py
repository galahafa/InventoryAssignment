from django.test import TestCase
from rest_framework.test import APIClient


class EndpointTest(TestCase):

    def test_inventory(self):
        test_cases = [{'endpoint': '/inventory', 'msg': '/inventory'},
                      {'endpoint': '/api/inventory', 'msg': 'api/inventory'},
                      {'endpoint': '/inventory/1', 'msg': '/inventory/1'}]
        client = APIClient()
        for test_case in test_cases:
            response = client.get(test_case.get('endpoint'))
            self.assertEqual(response.status_code, 200, msg=test_case.get('msg'))
