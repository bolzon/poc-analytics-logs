import logger


if __name__ == '__main__':

    log = logger.get_logger(__name__)

    log.info('This is an %s', 'info')
    log.error('This is an %s', 'error')

    log.analytics({'metadata': {'msg': 'sample message'}})
    log.analytics('foo bar')

    try:
        a = b + c
    except Exception as ex:
        log.error('error summing', exc_info=ex)
