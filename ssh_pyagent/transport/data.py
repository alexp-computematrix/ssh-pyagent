"""
SSH Transport Packet data types module

These data types represent low-level C programming data types and are used
to convert values into expected format as specified in OpenSSH agent protocol
"""
import typing as t


def byte(value: int) -> bytes:
    """
        Encode a single byte
    :param value: int
    :return: bytes
    """

    return bytes((value,))


def uint32(value: int) -> bytes:
    """
        Encode an integer as 4 bytes
        unsigned integer 32-bit
    :param value: int
    :return: bytes
    """

    return value.to_bytes(4, 'big')


def string(data: t.Union[bytes, str]) -> bytes:
    """
        Encode data with 4 bytes (uint32)
        pre-pended to specify data length
    :param data: Union[bytes, str]
    :return: bytes
    """

    if isinstance(data, str):
        data = data.encode('utf-8', errors='strict')

    return len(data).to_bytes(4, 'big') + data
