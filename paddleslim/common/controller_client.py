# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import socket
from .log_helper import get_logger

__all__ = ['ControllerClient']

_logger = get_logger(__name__, level=logging.INFO)


class ControllerClient(object):
    """
    Controller client.
    """

    def __init__(self,
                 server_ip=None,
                 server_port=None,
                 key=None,
                 client_name=None):
        """
        Args:
            server_ip(str): The ip that controller server listens on. None means getting the ip automatically. Default: None.
            server_port(int): The port that controller server listens on. 0 means getting usable port automatically. Default: 0.
            key(str): The key used to identify legal agent for controller server. Default: "light-nas"
            client_name(str): Current client name, random generate for counting client number. Default: None.
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self._key = key
        self._client_name = client_name

    def update(self, tokens, reward, iter):
        """
        Update the controller according to latest tokens and reward.
        Args:
            tokens(list<int>): The tokens generated in last step.
            reward(float): The reward of tokens.
        """
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((self.server_ip, self.server_port))
        tokens = ",".join([str(token) for token in tokens])
        socket_client.send("{}\t{}\t{}\t{}\t{}".format(
            self._key, tokens, reward, iter, self._client_name).encode())
        response = socket_client.recv(1024).decode()
        if response.strip('\n').split("\t") == "ok":
            return True
        else:
            return False

    def next_tokens(self):
        """
        Get next tokens.
        """
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((self.server_ip, self.server_port))
        socket_client.send("next_tokens".encode())
        tokens = socket_client.recv(1024).decode()
        tokens = [int(token) for token in tokens.strip("\n").split(",")]
        return tokens

    def request_current_info(self):
        """
        Request for current information.
        """
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((self.server_ip, self.server_port))
        socket_client.send("current_info".encode())
        current_info = socket_client.recv(1024).decode()
        return eval(current_info)
