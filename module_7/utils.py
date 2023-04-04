import logging
from logging_config import configure_logging

logger = logging.getLogger("utils")
# region task_1
# logging.basicConfig(level=logging.DEBUG)
# endregion

# region task_2-3-4
configure_logging()


# endregion

def get_number(message="Введите число: "):
    try:
        number = float(input(message))
        return number
    except ValueError:
        logger.error("Введено не число")
        exit()


def plus(a, b):
    result = a + b
    logger.debug(f"Результат операции plus {result}")
    return result


def subtract(a, b):
    result = a - b
    logger.debug(f"Результат операции subtract {result}")
    return result


def multiply(a, b):
    result = a * b
    logger.debug(f"Результат операции multiply {result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Результат операции divide {result}")
        return result
    except ZeroDivisionError:
        logger.warning("попытка поделить на ноль")
