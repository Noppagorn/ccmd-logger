import logging
import coloredlogs

class Logger:
    _instances = {}

    def __new__(cls, name='default'):
        if name not in cls._instances:
            cls._instances[name] = super(Logger, cls).__new__(cls)
            # Set up the logger
            cls._instances[name].logger = logging.getLogger(name)
            # Install coloredlogs with a nice format
            coloredlogs.install(
                level='INFO',
                fmt='%(asctime)s - %(levelname)s - %(message)s'
            )
        return cls._instances[name]

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def exception(self, message):
        self.logger.exception(message) 