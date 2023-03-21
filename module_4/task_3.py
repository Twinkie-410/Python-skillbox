import unittest

from flask_wtf import csrf
from task_1 import app

test_data = {'email': ('correct@mail.com', 'not_correct_mail_dotcom', None),
             'phone': ('1234567890', 'one_two_three_five', '90322', None),
             'name': ('somename', None),
             'address': ('someaddress', None),
             'index': ('123456', 'one-one-one', None),
             'comment': ('some comment', None)}


class TestRegistrationValidator(unittest.TestCase):
    @classmethod
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/registration'

    def test_fields_validator_correct_data(self):
        response = self.app.post(self.base_url, data={'email': test_data['email'][0],
                                                      'phone': test_data['phone'][0],
                                                      'name': test_data['name'][0],
                                                      'address': test_data['address'][0],
                                                      'index': test_data['index'][0],
                                                      'comment': test_data['comment'][0]})
        response_text = response.data.decode()
        self.assertTrue('Пользователь успешно зарегистрирован' in response_text)

    def test_input_required_if_fields_empty(self):
        response = self.app.post(self.base_url, data={'email': test_data['email'][2],
                                                      'phone': test_data['phone'][3],
                                                      'name': test_data['name'][1],
                                                      'address': test_data['address'][1],
                                                      'index': test_data['index'][2],
                                                      'comment': test_data['comment'][1]})
        response_text = response.data.decode()
        response_text_correct = "{'email': ['This field is required.'], 'phone': ['This field is required.'], 'name': ['This field is required.'], 'address': ['This field is required.'], 'index': ['This field is required.']}"
        self.assertEqual(response_text, response_text_correct)

    def test_email_number_index_validator_on_incorrect_data(self):
        response1 = self.app.post(self.base_url, data={'email': test_data['email'][1],
                                                      'phone': test_data['phone'][1],
                                                      'name': test_data['name'][0],
                                                      'address': test_data['address'][0],
                                                      'index': test_data['index'][1],
                                                      'comment': test_data['comment'][0]})

        response2 = self.app.post(self.base_url, data={'email': test_data['email'][0],
                                                       'phone': test_data['phone'][2],
                                                       'name': test_data['name'][0],
                                                       'address': test_data['address'][0],
                                                       'index': test_data['index'][0],
                                                       'comment': test_data['comment'][0]})

        response_text1 = response1.data.decode()
        response_text2 = response2.data.decode()

        response_text1_correct = "{'email': ['Invalid email address.'], 'phone': ['Not a valid integer value.', 'Number must be between 1000000000 and 9999999999.'], 'index': ['Not a valid integer value.']}"
        response_text2_correct = "{'phone': ['Number must be between 1000000000 and 9999999999.']}"
        self.assertEqual(response_text1, response_text1_correct)
        self.assertEqual(response_text2, response_text2_correct)
