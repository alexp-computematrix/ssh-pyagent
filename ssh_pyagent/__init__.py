import logging
import sys

logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_format = logging.Formatter(fmt='[SSH_PYAGENT]:[%(asctime)s]:[%(module)s]:[%(levelname)s] => %(message)s',
                                  datefmt='%Y-%m-%d | %H:%M:%S')

stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(stdout_format)
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)
