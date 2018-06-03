import logging


def get_result():
    try:
        result = 5 / 0
        return result
    except Exception:
        logging.exception('Exception', exc_info=True)
