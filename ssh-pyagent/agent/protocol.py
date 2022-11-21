"""
Base SSH Agent protocol module

SSH version 1 and SSH version 2 protocol objects
define the behaviour of an SSH agent object when
that object inherits its protocol from either
version or both.

An agent can inherit both protocol version to support
SSH client requests sending version 1/2 packet headers.

For reference to the SSH Agent protocol see URL below:
https://github.com/openssh/openssh-portable/blob/4e636cf/PROTOCOL.agent
"""
import logging
from abc import ABCMeta

logger = logging.getLogger(__name__)


class SSHAgentProtocol(metaclass=ABCMeta):
    """
    SSH Agent Protocol Base
    """

    def __init__(self):
        pass


class SSHAgentProtocolV1(SSHAgentProtocol):
    """
    SSH Agent Version 1 protocol object
    """

    def __init__(self):
        super().__init__()
        pass


class SSHAgentProtocolV2(SSHAgentProtocol):
    """
    SSH Agent Version 2 protocol object
    """

    def __init__(self):
        super().__init__()
        pass
