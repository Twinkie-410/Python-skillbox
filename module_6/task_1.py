import getpass
import hashlib
import logging

logger = logging.getLogger('password_logger')


def input_and_check_password():
    logger.debug("Начало input_and_check_password")
    password: str = input()
    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if hasher.hexdigest() == "898f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filename='stderr.txt',
                        format='%(asctime)s: %(levelname)s - %(message)s',
                        datefmt="%H:%M:%S")
    # logger.setLevel(logging.INFO)
    #
    # handler = logging.FileHandler('stderr.txt')
    # formatter = logging.Formatter("%(asctime)s - [%(levelname)s] -  %(name)s - %(message)s", "%HH:%MM:%SS")
    # handler.setFormatter(formatter)
    # handler.setLevel(logging.INFO)
    #
    # logger.addHandler(handler)

    count_number: int = 3
    logger.info(f'попытка ввести пароль, осталось попыток: {count_number}')
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
        logger.warning(f'пароль неверен, попыток осталось: {count_number}')
    logger.error('Пользователь трижды ввёл неправильный пароль')
    exit(1)

