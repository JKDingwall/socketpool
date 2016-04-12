# -*- coding: utf-8 -
#
# This file is part of socketpool.
# See the NOTICE for more information.

import socket

class kasocket(socket.socket):
    """Create a socket with keep alive options enabled."""
    def connect(self, address):
        super(kasocket, self).connect(address)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        try:
            self.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 600)
        except AttributeError:
            pass
