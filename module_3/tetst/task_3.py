import unittest

from module_2.task_7 import app, storage


class TestAccountingForFinancial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        storage.update({'20220823': 1500, '20220817': 3000, '20220515': 4000, '20210711': 8000,
                        '202208': 4500, '202205': 4000, '202107': 8000,
                        '2022': 8500, '2021': 8000})

    def test_can_add_correct_data(self):
        self.app.get('/add/20220812/2000')
        self.app.get('/add/20221008/500')
        self.app.get('/add/20200112/1000')
        correct_storage = {'20220823': 1500, '20220817': 3000, '20220515': 4000, '20210711': 8000, '20220812': 2000,
                           '20221008': 500, '20200112': 1000,
                           '202208': 6500, '202205': 4000, '202107': 8000, '202210': 500, '202001': 1000,
                           '2022': 11000, '2021': 8000, '2020': 1000}
        self.assertEqual(correct_storage, storage)

    def test_raise_error_add_if_incorrect_date(self):
        with self.assertRaises(ValueError):
            self.app.get('/add/220306/2000')

    def test_can_calculate_month(self):
        response = self.app.get('/calculate/2022/08')
        text_response_month = response.data.decode()
        correct_sum_month = str(storage['202208'])
        self.assertTrue(correct_sum_month in text_response_month)

    def test_can_calculate_year(self):
        response = self.app.get('/calculate/2022')
        text_response_month = response.data.decode()
        correct_sum_month = str(storage['2022'])
        self.assertTrue(correct_sum_month in text_response_month)

    def test_can_calculate_nonexistent_date_in_storage(self):
        response = self.app.get('/calculate/2010/14')
        text_response_month = response.data.decode()
        correct_sum_month = str(storage['201014'])
        self.assertTrue(correct_sum_month in text_response_month)
