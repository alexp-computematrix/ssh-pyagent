import io
import logging
import typing as t

from ssh_pyagent.consts import SSH_AGENT_MAX_MSG_LENGTH
from ssh_pyagent.transport import data

logger = logging.getLogger(__name__)


class SSHPacketException(Exception):
    """
    SSHTransportPacket related exceptions
    """


class SSHTransportPacket(io.BytesIO):
    """
    SSH Transport Packet dataclass object
    """

    def __init__(self, buffer: t.Union[bytes, bytearray]):
        super().__init__(buffer)
        self._data_buffer = buffer

        self._size = None
        self._length = None

    def __len__(self) -> int:
        return 0

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return

    @property
    def size(self) -> int:
        return self._size

    @property
    def length(self) -> int:
        return len(self)

    @property
    def header(self):
        return

    def translate_packet(self) -> None:
        """
        Translate the buffer into packet attributes
        :return: None
        """

        # TODO: parse buffer

        if self._size > SSH_AGENT_MAX_MSG_LENGTH:
            raise SSHPacketException('Packet exceeds max message length')
