'''
nhclientai
==========
The nhentai CLI client, for the terminal-dwelling degenerates.

Licensed under the GPL v3 license, located in the LICENSE file included with the software.

by hysrx and nhclientai's contributors.
'''

from nhclientai.handlers import Input, Downloader, Config
from nhclientai.doujinshi import Doujinshi
from nhclientai.interface import Screens

from pathlib import Path

import logging
import sys
import os

# Global Variables
userpath_map = {
    'darwin': f'{Path.home()}/Library/Application Support/nhclientai',
    'linux': f'{Path.home()}/.config/nhclientai',
    'win32': f'{Path.home()}/AppData/Roaming/nhclientai'
}

nhcli_scriptpath = Path(__file__).parent.absolute()
nhcli_userpath = Path(os.getenv(key='XDG_CONFIG_HOME', default=userpath_map[sys.platform]))

# Logging Initialization
logging.basicConfig(format='[%(levelname)s] (%(module)s:%(funcName)s:%(lineno)d) %(message)s',
                    filename=nhcli_userpath.joinpath('runtime.log'), filemode='w')

# Input Initialization
input_handler = Input()


class nhclientai:
    def __init__(self, config):
        pass

    def homepage(self, payload=None):
        pass

    def search(self, payload=None):
        pass

    def viewer(self, payload=None):
        pass

    def config(self, payload=None):
        pass


def cli():
    # Initialize
    config = Config()
    nhcli = nhclientai(config)

    # Program
    action_map = {
        'home': nhcli.homepage,
        'search': nhcli.search,
        'view': nhcli.viewer,
        'config': nhcli.config
    }

    result = 'homepage'  # Show Homepage on Startup
    payload = None

    while True:
        result = action_map[result](payload)

        if result not in [key for key in action_map]:
            result = nhcli.viewer(result)
