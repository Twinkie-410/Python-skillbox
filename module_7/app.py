import logging
import sys
from logging_config import configure_logging
import utils
import logging_tree

logger = logging.getLogger("app")
# region task_1
# logging.basicConfig(level=logging.DEBUG)
# endregion

# region task_2-3-4
configure_logging()


# endregion

def calculate():
    logger.debug("Тест ascii фильтра - не должно отображаться")
    logger.debug("test ascii filter - it should be visible")
    operation = input("Выберите операцию: '+', '-','*', '/'\n> ")
    operations = {"+": utils.plus, "-": utils.subtract, "*": utils.multiply, "/": utils.divide}
    if operation not in operations:
        logger.error(f"Введена некорректная операция: {operation}")
        exit()

    a = utils.get_number()
    logger.debug(f"Число успешно обработано: {a}")
    b = utils.get_number()
    logger.debug(f"Число успешно обработано: {b}")

    result = operations[operation](a, b)
    logger.info(f"Первыое число a={a}, второе число b={b}, операция: '{operation}', результат опреации = {result}")
    return result


if __name__ == '__main__':
    print(calculate())

    # region task_6
    with open("logging_tree.txt", "w") as file:
        file.write(logging_tree.format.build_description())
    # endregion

