"""valhal - a semantic game engine

   Copyright (c) 2015 Florian Berger <mail@florian-berger.de>

   To run valhal games, use one of the following command line commands:

       $ python3 -m valhal.run server

       $ python3 -m valhal.run client

       $ python3 -m valhal.run standalone
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

# Work started on 04. Sep 2015.

import valhal
import valhal.net
import sys
# Standalone:
import threading

def main():
    """Main method, for IDE convenience.
    """

    if len(sys.argv) < 2:

        raise RuntimeError("Argument 'server', 'client' or 'standalone' missing.")

    if sys.argv[1] == "server":

        if "--net" in sys.argv:

            valhal.net.NetServer().serve()

        else:

            valhal.Server().serve()

    elif sys.argv[1] == "client":

        if "--net" in sys.argv:

            valhal.net.NetClient().connect()

        else:

            valhal.Client().run()

    elif sys.argv[1] == "standalone":

        server = valhal.Server()

        client = valhal.Client()

        client.__dict__["server"] = server

        client_thread = threading.Thread(target = client.run, name = "valhal-client-{0}".format(client.uuid))

        valhal.LOGGER.info("Starting client thread.")

        client_thread.start()

        server_thread = threading.Thread(target = server.serve, name = "valhal-server")

        valhal.LOGGER.info("Starting server thread.")

        server_thread.start()

        valhal.LOGGER.info("Waiting for server thread to terminate.")

        server_thread.join()
        
        valhal.LOGGER.info("Waiting for client thread to terminate.")

        client_thread.join()

        valhal.LOGGER.info("All threads terminated, exiting.")

    else:

        raise RuntimeError("Argument '{}' not supported".format(sys.argv[1]))

    return

if __name__ == "__main__":

    main()
