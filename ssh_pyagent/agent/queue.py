"""
SSH Agent queue module

Each SSH Agent will have a request queue for which
an SSH client will send requests, and store said
requests in the queue until they can be processed.
"""
import logging
import queue

from ssh_pyagent.consts import SSH_AGENT_MAX_REQUEST_QUEUE

logger = logging.getLogger(__name__)


class SSHAgentRequestQueue(queue.Queue):
    """
    SSH Agent Request Queue object
    """

    def __init__(self):
        super().__init__(maxsize=SSH_AGENT_MAX_REQUEST_QUEUE)
