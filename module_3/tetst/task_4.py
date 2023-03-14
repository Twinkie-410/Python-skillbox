import unittest

from module_3.code_by_task_4 import Person


class TestPersonsMethods(unittest.TestCase):
    def test_init(self):
        person1 = Person('somename', 2010, 'brodskaya 35-64')
        self.assertEqual(person1.name, 'somename')
        self.assertEqual(person1.yob, 2010)
        self.assertEqual(person1.address, 'brodskaya 35-64')

    def test_get_age(self):
        person1 = Person('somename', 2012, '')
        self.assertEqual(person1.get_age(), 11)

    def test_get_name(self):
        person1 = Person('Ivan', 2012, '')
        self.assertEqual(person1.get_name(), 'Ivan')

    def test_get_address(self):
        person1 = Person('somename', 2012, 'rechnaya, house 12, flat 58')
        self.assertEqual(person1.get_address(), 'rechnaya, house 12, flat 58')

    def test_set_name(self):
        person1 = Person('somename', 2012, '')
        person1.set_name('Ivan')
        self.assertEqual(person1.name, 'Ivan')

    def test_set_address(self):
        person1 = Person('somename', 2012, '')
        person1.set_address('rechnaya, house 12, flat 58')
        self.assertEqual(person1.address, 'rechnaya, house 12, flat 58')

    def test_is_homeless_be_true(self):
        person1 = Person('somename', 2012, '')
        self.assertEqual(person1.is_homeless(), True)

    def test_is_homeless_be_false(self):
        person1 = Person('somename', 2012, 'rechnaya, house 12, flat 58')
        self.assertEqual(person1.is_homeless(), False)
