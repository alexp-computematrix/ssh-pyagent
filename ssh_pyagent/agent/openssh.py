"""
Base OpenSSH Agent module
"""
import logging

from ssh_pyagent.agent.protocol import OpenSSHAgentProtocolV1, \
    OpenSSHAgentProtocolV2
from ssh_pyagent.agent.queue import SSHAgentRequestQueue

logger = logging.getLogger(__name__)


class OpenSSHAgent(OpenSSHAgentProtocolV1, OpenSSHAgentProtocolV2):
    """
    Base OpenSSH Agent object
    """

    def __init__(self, transport):
        self.__transport = transport
        self.__request_queue = SSHAgentRequestQueue()

        self.__keys = []

    @property
    def transport(self):
        return self.__transport

    @transport.setter
    def transport(self, transport):
        # TODO: strictly enforce transport setting
        self.__transport = transport

    @property
    def keys(self):
        # TODO: create keypair objects
        return self.__keys

    def __process_client_request(self):
        """
            Process requests recieved from an
            OpenSSH client via transport
        :return:
        """
