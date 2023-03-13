import unittest

from module_2.task_3 import decrypt


class TestDycrypt(unittest.TestCase):

    def _help_equal(self, ciphers, correct_decode):
        for i, cipher in enumerate(ciphers):
            with self.subTest(cipher=cipher):
                self.assertEqual(correct_decode[i], decrypt(cipher))

    def test_cipher_one_dote(self):
        ciphers = ["абра-кадабра.", "."]
        correct_decode = ["абра-кадабра", ""]
        self._help_equal(ciphers, correct_decode)

    def test_cipher_two_dotes(self):
        ciphers = ["абраа..-кадабра", "абра--..кадабра"]
        correct_decode = ["абра-кадабра", "абра-кадабра"]
        self._help_equal(ciphers,  correct_decode)
    def test_cipher_three_dotes(self):
        ciphers = ["абраа..-.кадабра", "1..2.3"]
        correct_decode = ["абра-кадабра", "23"]
        self._help_equal(ciphers,  correct_decode)


    def test_cipher_many_dotes(self):
        ciphers = ["абра........", "абр......a.", "1......................."]
        correct_decode = ["", "a", ""]
        self._help_equal(ciphers, correct_decode)
