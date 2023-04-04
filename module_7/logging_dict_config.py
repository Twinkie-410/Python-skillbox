import logging
import sys
from file_by_level_handler import FileByLevelHandler


# region task_7
class IsASCII(logging.Filter):
    def filter(self, record):
        return str.isascii(record.msg)  # или return all(symbol in string.printable for symbol in record.msg)
# endregion


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    # region task_7
    "filters": {
        "ascii": {"()": IsASCII}
    },
    # endregion
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout,
            # region task_7
            "filters": ["ascii"]
            # endregion
        },

        "files_by_level": {
            "()": FileByLevelHandler,
            "level": "DEBUG",
            "formatter": "base",
        },
        # region task_5
        "time_rotating": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "base",
            "filename": "utils.log",
            "when": "h",
            "interval": 10,
            "backupCount": 1
        }
        # endregion
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console", "files_by_level"]
        },
        # region task_4
        # "utils": {
        #     "level": "DEBUG",
        #     "handlers": ["console", "files_by_level"]
        # }
        # endregion

        # region task_5
        "utils": {
            "level": "INFO",
            "handlers": ["time_rotating"]
        }
        # endregion
    }
}
