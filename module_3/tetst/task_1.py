import datetime
import unittest
from freezegun import freeze_time

from module_2.task_4 import app

good_weekday = {
    0: "Хорошего понедельника",
    1: "Хорошего вторника",
    2: "Хорошей среды",
    3: "Хорошего четверга",
    4: "Хорошеё пятницы",
    5: "Хорошей субботы",
    6: "Хорошего воскресенья"}


class TestHelloGoodDay(unittest.TestCase):
    @freeze_time("2023-03-06")
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello_world/'

    def _get_weekday(self):
        current_day = datetime.datetime.today().weekday()
        return good_weekday[current_day]

    def test_can_get_correct_username_with_weekdate(self):
        username = 'Some'
        url = self.base_url + username
        response = self.app.get(url)
        response_text = response.data.decode()
        weekday = self._get_weekday()
        if username in good_weekday.values():
            self.assertTrue(weekday in response_text.split()[-2:])
        print(response_text)
        self.assertTrue(weekday in response_text)
