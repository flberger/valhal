"""valhal - a semantic game engine

   Copyright (c) 2015 Florian Berger <mail@florian-berger.de>

   See documentation of valhal.run on how to run client, server, and
   stanalone modes.
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
# Client:
import uuid

VERSION = "0.1.0"

LOGGER = logging.getLogger("valhal")
LOGGER.setLevel(logging.DEBUG)
STDERR_FORMATTER = logging.Formatter("{name} [{levelname}] {funcName}(): {message} (l.{lineno})", style = "{")
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

       Attributes:

       Client.server
           An instance of valhal.Server. Needs to be injected before
           Client.run() is being called.

       Client.uuid
           This Client's random UUID.
    """

    def __init__(self):
        """Initialising.
        """

        self.logger = logging.getLogger("valhal.client")
        self.logger.setLevel(logging.DEBUG)

        # server needs to be injected before Client.run() is being
        # called.
        #
        self.server = None

        # Generate a random UUID
        #
        self.uuid = uuid.uuid4()

        self.logger.info("Client {0} initialised.".format(str(self.uuid)))

        return

    def run(self):
        """Run the client by connecting to and interacting with the server, and providing a user interface.
        """

        if self.server is None:

            raise RuntimeError("Client.server is not set, cannot run without a server connection. You must set Client.server before Client.run() can be called.")

        self.server.register(self)

        self.logger.debug("Successfully registered with server.")

        return

    def update(self, update):
        """Present the server update to the user.

           This method returns nothing, the server will collect a
           reaction by calling Client.respond().
        """

        return

    def respond(self):
        """Return a dict containing the client response.
        """

        response = {}

        return response

class Server:
    """The game server.

       Attributes:

       Server.clients
           A dict mapping identifiers to valhal.Client instances
           connected to this server.

       Server.max_clients
           The maximum number of connected valhal.Clients this server
           will accept. If set below 1, the server will accept and
           unlimited number of clients. The default is 1 client.

       Server.current_tick
           An integer giving the current tick of the server. The first
           tick is 0. Server.current_tick may overflow at some point
           an restart at 0.
    """

    def __init__(self, max_clients = 1):
        """Initialise.
        """

        self.logger = logging.getLogger("valhal.server")
        self.logger.setLevel(logging.DEBUG)

        self.clients = {}

        self.max_clients = max_clients

        self.current_tick = 0

        self.logger.info("Starting up, serving up to {0} clients.".format(self.max_clients))

        return

    def register(self, client):
        """Register a new client.
           client is expected to be an instance of valhal.Client.
        """

        if len(self.clients) > 0 and len(self.clients) >= self.max_clients:

            msg = "Can not connect another client: limit of {0} clients reached".format(self.max_clients)

            self.logger.error(msg)

            raise RuntimeError(msg)

        self.clients[client.uuid] = client

        self.logger.info("Registering client {0}".format(client.uuid))

        return

    def serve(self):
        """Serve to connected clients.
           Clients will be served round-robin, one at a time.
        """

        self.logger.warning("TODO: running for 10 rounds only.")

        for i in range(10):

            for client_id in self.clients.keys():

                # Read from the current client ...
                #
                incoming = self.clients[client_id].respond()

                update = self.tick((client_id, incoming))

                # --- but send the update to all clients.
                #
                for client in self.clients.values():

                    client.update(update)

        return

    def tick(self, id_incoming):
        """Return a dict with state updates, possibly reacting to the (client_id, incoming) tuple given.
        """

        update = {}

        self.logger.debug("Tick #{0}".format(self.current_tick))

        self.current_tick += 1

        return update
