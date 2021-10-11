import logging
import os
import sys

from pythonjsonlogger import jsonlogger
from typing import Dict, Tuple


LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()

STATIC_FIELDS = {
    'app_version': '1.0',
    'log_type': 'app'
}

REMOVED_ATTRS = (
    'lineno', 'levelname', 'filename', 'threadName')

RESERVED_ATTRS = (
    'args', 'asctime', 'created', 'exc_info', 'exc_text',
    'funcName', 'levelno', 'module', 'msecs', 'msg',
    'name', 'pathname', 'process', 'processName', 'relativeCreated',
    'stack_info', 'thread')

class CustFormatter(jsonlogger.JsonFormatter):
    def process_log_record(self, log_record: Dict):
        if log_record.get('message') is None:
            del log_record['message']
        if log_record.get('log_type') == 'analytics':
            for k in REMOVED_ATTRS:
                del log_record[k]
        return log_record


class CustLogger(logging.getLoggerClass()):
    def analytics(self, msg: Dict):
        if type(msg) is not dict:
            msg = {'message': str(msg)}
        msg['log_type'] = 'analytics'
        self.info(msg)


stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(CustFormatter(timestamp=True,
                                         reserved_attrs=RESERVED_ATTRS,
                                         static_fields=STATIC_FIELDS))

logging.setLoggerClass(CustLogger)
logging.basicConfig(level=LOG_LEVEL, handlers=[stream_handler])


def get_logger(logger_name: str) -> CustLogger:
    logger = logging.getLogger(logger_name)
    return logger
