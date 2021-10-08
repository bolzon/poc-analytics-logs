import os
import logging
from pythonjsonlogger import jsonlogger
from typing import Dict, Tuple


LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()

STATIC_FIELDS = {
    'app_version': '1.0',
    'log_type': 'app'
}


class NieFormatter(jsonlogger.JsonFormatter):
    def process_log_record(self, log_record: Dict):
        del log_record['message']
        return log_record


class NieLogger(logging.getLoggerClass()):
    def trace(self, msg: Tuple[str, Dict], exception: Exception = None):
        if exception is not None:
            self.error({'error': msg}, None, exc_info=exception)
        else:
            self.info({'info': msg})

    def analytics(self, msg: Dict):
        msg['log_type'] = 'analytics'
        self.info(msg)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(NieFormatter(timestamp=True,
                                         static_fields=STATIC_FIELDS))

logging.setLoggerClass(NieLogger)
logging.basicConfig(level=LOG_LEVEL, handlers=[stream_handler])


def get_logger(logger_name: str) -> NieLogger:
    logger = logging.getLogger(logger_name)
    return logger
