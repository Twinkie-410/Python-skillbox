from typing import Type


class BlockErrors:
    def __init__(self, error_types: set[Type[Exception]] = None):
        self.error_types = error_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if True not in [issubclass(exc_type, error_type) for error_type in self.error_types]:
            return False
        return True


# err_types = {Exception}
# with BlockErrors(err_types):
#     a = 1 / '0'
# print('Выполнено без ошибок')
