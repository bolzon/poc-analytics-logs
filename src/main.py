import logger
from time import sleep


if __name__ == '__main__':

    log = logger.get_logger(__name__)

    while True:

        log.analytics({
            'metadata': {
                'msg': 'sample message'
            }
        })

        log.trace('will now raise an exception')

        try:
            a = b + c
        except Exception as ex:
            log.trace('error summing', ex)

        sleep(5)
