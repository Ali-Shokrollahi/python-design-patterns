"""
Task:
    - Build a logging system where log messages pass through multiple levels
     of handlers (e.g., Debug, Info, Warning, Error).
"""
from abc import ABC, abstractmethod


class LoggingMessage:
    def __init__(self, message: str, level: str):
        self.message = message
        self.level = level


class AbstractLoggerHandler(ABC):
    @abstractmethod
    def handle(self, log_message: LoggingMessage):
        ...

    @abstractmethod
    def set_next_handler(self, handler: 'AbstractLoggerHandler'):
        ...


class BaseLoggingHandler(AbstractLoggerHandler):
    _next_handler = None

    @abstractmethod
    def handle(self, log_message: LoggingMessage):
        if self._next_handler:
            return self._next_handler.handle(log_message)
        return None

    def set_next_handler(self, handler: AbstractLoggerHandler):
        self._next_handler = handler
        return handler


class DebugLoggingHandler(BaseLoggingHandler):
    def handle(self, log_message: LoggingMessage):
        if log_message.level == 'debug':
            print(f"[DEBUG]: {log_message.message}")
        else:
            return super().handle(log_message)


class InfoLoggingHandler(BaseLoggingHandler):
    def handle(self, log_message: LoggingMessage):
        if log_message.level == 'info':
            print(f"[INFO]: {log_message.message}")
        else:
            return super().handle(log_message)


class WarningLoggingHandler(BaseLoggingHandler):
    def handle(self, log_message: LoggingMessage):
        if log_message.level == 'warning':
            print(f"[WARNING]: {log_message.message}")
        else:
            return super().handle(log_message)


class ErrorLoggingHandler(BaseLoggingHandler):
    def handle(self, log_message: LoggingMessage):
        if log_message.level == 'error':
            print(f"[ERROR]: {log_message.message}")
        else:
            return super().handle(log_message)


def build_logger_chain():
    error_logger_handler = ErrorLoggingHandler()
    warning_logger_handler = WarningLoggingHandler()
    info_logger_handler = InfoLoggingHandler()
    debug_logger_handler = DebugLoggingHandler()
    warning_logger_handler.set_next_handler(error_logger_handler)
    info_logger_handler.set_next_handler(warning_logger_handler)
    debug_logger_handler.set_next_handler(info_logger_handler)

    return debug_logger_handler


if __name__ == '__main__':
    logger_chain = build_logger_chain()

    logger_chain.handle(LoggingMessage('This is information', 'info'))
    logger_chain.handle(LoggingMessage('This is Error', 'error'))
