from logger import get_logger


if __name__ == '__main__':

    logger = get_logger(__name__)

    logger.info('This is an %s', 'info')
    logger.error('This is an %s', 'error')

    logger.debug({
        'dict': {
            'version': '1.2.3',
            'memory': 1024
        }
    })

    logger.analytics({'metadata': {'msg': 'sample message'}})
    logger.analytics('foo bar')

    try:
        a = b + c
    except Exception as ex:
        logger.error('error summing %s', 'numbers', exc_info=ex)
