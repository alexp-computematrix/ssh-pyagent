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

logger = logging.getLogger(__name__)


class OpenSSHAgentProtocol:
    """
    SSH Agent Protocol Base
    """

    def ssh_agent_success(self):
        return

    def ssh_agent_failure(self):
        return


class OpenSSHAgentProtocolV1(OpenSSHAgentProtocol):
    """
    SSH Agent Version 1 protocol object
    """

    def ssh_agent_rsa_identities_answer(self, request, keys):
        return

    def ssh_agent_rsa_response(self):
        return


class OpenSSHAgentProtocolV2(OpenSSHAgentProtocol):
    """
    SSH Agent Version 2 protocol object
    """

    def ssh2_agent_identities_answer(self, request, keys):
        return

    def ssh2_agent_sign_response(self, request, keys):
        return
