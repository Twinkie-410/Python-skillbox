import unittest
from task_2 import app


class TestCodeExecutor(unittest.TestCase):
    @classmethod
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/code'

    def test_time_out(self):
        response1 = self.app.post(self.base_url, data={'code': b"from time import sleep\nsleep(5)\nprint('hello')",
                                                       'time_out': 4})
        response2 = self.app.post(self.base_url, data={'code': "print('hello')",
                                                       'time_out': 32})
        response1_correct = "команда выполнялась дольше указанного времени"
        response2_correct = "{'time_out': ['Number must be between 1 and 30.']}"

        self.assertEqual(response1_correct, response1.data.decode())
        self.assertEqual(response2_correct, response2.data.decode())

    def test_on_shell_true(self):
        response = self.app.post(self.base_url, data={'code': 'print()"; echo "hacked',
                                                      'time_out': 3})
        self.assertTrue('hacked' not in response.data.decode())

    def test_validator(self):
        response1 = self.app.post(self.base_url, data={'code': "print('hello')",
                                                       'time_out': 32})
        response2 = self.app.post(self.base_url, data={'code': "print('hello')",
                                                       'time_out': None})
        response3 = self.app.post(self.base_url, data={'code': None,
                                                       'time_out': 5})
        response1_correct = "{'time_out': ['Number must be between 1 and 30.']}"
        response2_correct = "{'time_out': ['This field is required.']}"
        response3_correct = "{'code': ['This field is required.']}"

        self.assertTrue(response1_correct, response1.data.decode())
        self.assertTrue(response2_correct, response2.data.decode())
        self.assertTrue(response3_correct, response3.data.decode())
