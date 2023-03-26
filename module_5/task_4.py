import sys
import traceback


class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        self.prev_stdout = sys.stdout
        self.prev_stderr = sys.stderr
        if self.stdout != None:
            sys.stdout = self.stdout
        if self.stderr != None:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stdout != None:
            self.stdout.close()
        sys.stderr.write(traceback.format_exc())
        if self.stderr != None:
            self.stderr.close()
        sys.stdout = self.prev_stdout
        sys.stderr = self.prev_stderr
        return True


if __name__ == '__main__':
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')
