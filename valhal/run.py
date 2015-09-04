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

# Work started on 04. Sep 2015.

import valhal
import sys

def main():
    """Main method, for IDE convenience.
    """

    if len(sys.argv) < 2:

        raise RuntimeError("Argument 'server', 'client' or 'standalone' missing.")

    if sys.argv[1] == "server":

        sys.stderr.write("TODO: Run server\n")

    elif sys.argv[1] == "client":

        sys.stderr.write("TODO: Run client\n")

    elif sys.argv[1] == "standalone":

        sys.stderr.write("TODO: Run standalone\n")

    else:

        raise RuntimeError("Argument '{}' not supported".format(sys.argv[1]))

    return

if __name__ == "__main__":

    main()
