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

# Work started on 03. Sep 2015.

import logging
# Server
import socketserver
import json

VERSION = "0.1.0"

LOGGER = logging.getLogger("valhal")
LOGGER.setLevel(logging.DEBUG)
STDERR_FORMATTER = logging.Formatter("valhal [%(levelname)s] %(funcName)s(): %(message)s (l.%(lineno)d)")
STDERR_HANDLER = logging.StreamHandler()
STDERR_HANDLER.setFormatter(STDERR_FORMATTER)
LOGGER.addHandler(STDERR_HANDLER)

class Scene:
    """A timespan in valhal.Game, with start and end behaviour.

       Attributes:

       Scene.set
           An instance of valhal.Set.
    """

    def __init__(self, set):
        """Initialise.
        """

        self.set = set

        return

class Set:
    """A place inhabited by valhal.Actor and valhal.Prop instances.
    """

    pass

class Actor:
    """An entity, acting with a defined behaviour, controlled by a human or computer.
    """

    pass

class Prop:
    """An entity, static and without behaviour.
    """

    pass


class Game:
    """Represents a running game.
    """

    pass

class Client:
    """The game client.
    """

    pass

class Server:
    """The game server.

       Attributes:

       Server.port
           The TCP port to listen on.
    """

    def __init__(self, port = 22000):
        """Initialise the server.
           port is the TCP port to listen on.
        """

        self.logger = logging.getLogger("valhal.server")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(STDERR_HANDLER)

        logger_wrapper = self.logger

        class ValhalRequestHandler(socketserver.StreamRequestHandler):

            def handle(self):
                """Handle a request using the Python file API.
                """

                data = self.rfile.readline().strip()

                logger_wrapper.debug("{0} incoming: '{1}'".format(self.client_address, data))

                self.wfile.write(json.dumps({"Error": "TODO: ValhalRequestHandler.handle() must return something useful"}) + "\n")

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
