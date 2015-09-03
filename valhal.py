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


VERSION = "0.1.0"

LOGGER = logging.getLogger("valhal")
LOGGER.setLevel(logging.DEBUG)
STDERR_FORMATTER = logging.Formatter("valhal [%(levelname)s] %(funcName)s(): %(message)s (l.%(lineno)d)")
STDERR_HANDLER = logging.StreamHandler()
STDERR_HANDLER.setFormatter(STDERR_FORMATTER)
LOGGER.addHandler(STDERR_HANDLER)

def main():
    """Main function, for IDE convenience.
    """

    return

if __name__ == "__main__":

    main()

