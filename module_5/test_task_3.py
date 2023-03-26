import unittest

from task_3 import BlockErrors


class TestBlockErrors(unittest.TestCase):
    # def _help_function_for_test(self, run_code, error_types: set[Type[Exception]] = None):
    #     with BlockErrors(error_types):
    #         run_code.
    def test_error_ignore(self):
        def test_case():
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            return True

        return self.assertTrue(test_case())

    def test_level_up_error(self):
        with self.assertRaises(TypeError):
            with BlockErrors():
                a = 1 / '0'
            return True

    def test_ignore_error_in_the_outer_block(self):
        def test_case():
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                return 'Внутренний блок: выполнено без ошибок'
            return True

        return self.assertTrue(test_case())

    def test_subclasses_error(self):
        def test_case():
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
            return True
        return self.assertTrue(test_case())

