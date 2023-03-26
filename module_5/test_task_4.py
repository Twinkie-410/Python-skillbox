import unittest
from task_4 import Redirect


class TestRedirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

    def test_redirect_stdout(self):
        with open('stdout.txt', 'r') as stdout:
            self.assertTrue('Hello stdout.txt' in stdout.read())

    def test_redirect_stderr(self):
        with open('stderr.txt', 'r') as stderr:
            self.assertTrue('Hello stderr.txt' in stderr.read())


if __name__ == '__main__':
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
