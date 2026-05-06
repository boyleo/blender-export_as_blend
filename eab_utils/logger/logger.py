from .logger_base import Logger, SCROLL_OFFSET_INCREMENT


class LoggerProgress(Logger):
    def __init__(self, log_name="ROOT"):
        super(LoggerProgress, self).__init__(log_name)
