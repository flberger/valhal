"""valhal - a semantic game engine

   Copyright (c) 2015 Florian Berger <mail@florian-berger.de>
"""

# This file is part of valhal.
#
# valhal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# valhal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with valhal.  If not, see <http://www.gnu.org/licenses/>.

# Work started on 05. Sep 2015.

import valhal
# Server:
import socketserver
import json
# Client:
import socket

class NetClient(valhal.Client):
    """A valhal.Client which interacts with a valhal.Server though the network.
    """

    def connect(self):
        """Establish a connection to the server, possibly involving user interaction.
        """

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # TODO: Using localhost
            sock.connect(("localhost", 22000))
            sock.sendall(bytes(json.dumps({"HELO": "Client calling"}) + "\n", encoding = "utf8"))

        finally:
            sock.close()

        return

class NetServer(valhal.Server):
    """A valhal.Server which interacts with clients though the network.

       Attributes:

       Server.port
           The TCP port to listen on.
    """

    def __init__(self, port = 22000):
        """Initialise the server.
           port is the TCP port to listen on.
        """

        valhal.Server.__init__(self)

        logger_wrapper = self.logger

        class ValhalRequestHandler(socketserver.StreamRequestHandler):

            def handle(self):
                """Handle a request using the Python file API.
                """

                data = str(self.rfile.readline(), encoding = "utf8").strip()

                logger_wrapper.debug("{0} incoming: '{1}'".format(self.client_address, data))

                self.wfile.write(bytes(json.dumps({"Error": "TODO: ValhalRequestHandler.handle() must return something useful"}) + "\n", encoding = "utf8"))

                return

            # End of class ValhalRequestHandler

        self.port = port

        # Listen on all interfaces
        #
        self.server = socketserver.TCPServer(("0.0.0.0", self.port), ValhalRequestHandler)

        return

    def serve(self):
        """Serve, listening to Server.port.
        """

        self.logger.info("Serving on port {0}".format(self.port))

        self.server.serve_forever()

        return
