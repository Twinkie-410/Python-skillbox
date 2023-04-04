import logging.config
import sys
from file_by_level_handler import FileByLevelHandler
from logging_dict_config import dict_config


def configure_logging():
    # region task_2-3
    # stream_handler = logging.StreamHandler(sys.stdout)
    # formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
    # stream_handler.setFormatter(formatter)
    #
    # # region task_3
    # my_handler = FileByLevelHandler()
    # my_handler.setFormatter(formatter)
    # # endregion
    #
    # logging.basicConfig(level=logging.DEBUG, handlers=[stream_handler, my_handler])

    # region task_4
    logging.config.dictConfig(dict_config)
    # endregion
    
    # endregion
