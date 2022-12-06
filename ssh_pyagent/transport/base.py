"""
Base OpenSSH Agent Transport module
"""
import logging
from abc import ABCMeta
from enum import Enum

logger = logging.getLogger(__name__)


class TransportChannel(metaclass=ABCMeta):
    """
    OpenSSH Agent Transport Channel object
    """

    class States(Enum):
        # TODO: may require read/write state tracking
        OPEN = 0
        CLOSED = 1

    def __init__(self):
        self.__state = self.States.CLOSED

    @property
    def state(self):
        return self.__state

    def open(self):
        """
            Open the transport channel
        :return:
        """
        self.__state = self.States.OPEN

    def poll(self):
        """
            Poll for data in the transport channel
        :return:
        """
        raise NotImplementedError

    def signal(self):
        """
            Signal data in the transport channel
        :return:
        """
        raise NotImplementedError

    def transmit(self):
        """
            Transmit data into the transport channel buffer
        :return:
        """
        raise NotImplementedError

    def close(self):
        """
            Close the transport channel
        :return:
        """
        self.__state = self.States.CLOSED
