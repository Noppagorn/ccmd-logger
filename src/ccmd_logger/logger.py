import logging
import coloredlogs
import traceback
import sys

class Logger:
    _instances = {}

    def __new__(cls, name='default'):
        if name not in cls._instances:
            cls._instances[name] = super(Logger, cls).__new__(cls)
            # Set up the logger
            cls._instances[name].logger = logging.getLogger(name)
            # Install coloredlogs with a nice format and custom level styles
            coloredlogs.install(
                level='INFO',
                logger=cls._instances[name].logger,
                fmt='%(asctime)s - %(levelname)s - %(message)s',
                level_styles={
                    'debug': {'color': 'white'},
                    'info': {'color': 'green'},
                    'warning': {'color': 'yellow'},
                    'error': {'color': 'red', 'bold': True},
                    'critical': {'color': 'red', 'bold': True, 'background': 'white'},
                }
            )
        return cls._instances[name]

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        stack_trace = ''.join(traceback.format_stack()[:-1])
        self.logger.error(f"{message}\nStack trace:\n{stack_trace}")

    def critical(self, message):
        stack_trace = ''.join(traceback.format_stack()[:-1])
        self.logger.critical(f"{message}\nStack trace:\n{stack_trace}")

    def exception(self, message):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        if exc_traceback:
            stack_trace = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            self.logger.error(f"{message}\nException stack trace:\n{stack_trace}")
        else:
            stack_trace = ''.join(traceback.format_stack()[:-1])
            self.logger.error(f"{message}\nStack trace:\n{stack_trace}") 