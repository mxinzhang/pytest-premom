import logging
import time
import os

# Define the base path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Define the log file path
LOG_PATH = os.path.join(BASE_PATH, "log")
# Create the log directory
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():
    """
    Logger class for logging messages to a file and console.
    """

    def __init__(self):
        """
        Initialize the Logger object.
        """
        # Set the log file name based on the current date
        self.logname = os.path.join(
            LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))

        # Create a logger object
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        # Create a log message formatter
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        # Create a file logger and set its level and formatter
        self.filelogger = logging.FileHandler(
            self.logname, mode='a', encoding="UTF-8")
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)

        # Create a console logger and set its level and formatter
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.console.setFormatter(self.formater)

        # Add the file logger and console logger to the logger object
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")
