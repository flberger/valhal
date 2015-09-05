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
    """

    def __init__(self):
        """Initialising.
        """

        # server needs to be injected before Client.run() is being
        # called.
        #
        self.server = None

        self.logger = logging.getLogger("valhal.client")
        self.logger.setLevel(logging.DEBUG)

        return
        
    def run(self):
        """Run the client by connecting to and interacting with the server, and providing a user interface.
        """

        if self.server is None:

            raise RuntimeError("Client.server is not set, cannot run without a server connection. You must set Client.server before Client.run() can be called.")

        return

class Server:
    """The game server.
    """

    def __init__(self):
        """Initialise.
        """

        self.logger = logging.getLogger("valhal.server")
        self.logger.setLevel(logging.DEBUG)

        return
