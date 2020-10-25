'''
nhclientai
==========
The nhentai CLI client, for the terminal-dwelling degenerates.

Licensed under the GPL v3 license, located in the LICENSE file included with the software.

by hysrx and nhclientai's contributors.
'''

from handlers import Input, Downloader, Config
from doujinshi import Doujinshi
from interface import Screens

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
nhcli_configpath = nhcli_userpath.joinpath('config.toml')

# Logging Initialization
logging.basicConfig(format='[%(levelname)s] (%(module)s:%(funcName)s:%(lineno)d) %(message)s',
                    filename=nhcli_userpath.joinpath('runtime.log'), filemode='w')

# Input Initialization
input_handler = Input()

# Checks
if nhcli_userpath.is_dir() is False:
    logging.info(f'Made directory {nhcli_userpath} due to its nonexistance.')
    os.mkdir(nhcli_userpath)

class nhclientai:
    class Signals:
        class UserExit(Exception):
            pass

    def __init__(self, config):
        self.config = config

    def homepage(self, payload=None):
        pass

    def search(self, payload=None):
        pass

    def viewer(self, payload=None):
        pass

    def config(self, payload=None):
        pass

    class Utilities:
        def clear_terminal():
            os.system('cls') if sys.platform == 'win32' else os.system('clear')

        def display_wizard():
            def ask(question):
                while True:
                    result = input(question)

                    try:
                        int(result)
                    except ValueError:
                        print('Value must be able to be represented as an integer!')
                    else:
                        break

                return int(result)

            try:
                input('Please make the current terminal window fullscreen before proceeding.')

                display_width = ask('Please input the width of your monitor in pixels. (e.g. 1920)')
                display_height = ask('Please input the width of your height in pixels. (e.g. 1080)')

                columns, lines = os.get_terminal_size()  # columns = width, lines = height

                cell_width = display_width / columns
                cell_height = display_height / lines

            except KeyboardInterrupt:
                return nhclientai.Signals.UserExit

            else:
                return {
                    'display_height': display_height,
                    'display_width': display_width,
                    'cell_width': cell_width,
                    'cell_height': cell_height
                }

        def make_config():
            while True:
                try:
                    display_data = nhclientai.Utilities.display_wizard()

                except nhclientai.Signals.UserExit:
                    print('The display wizard is required for first setup.')

                else:
                    break

            config_text = f'''# nhclientai Configuration TOML
[cache]
lifespan = 24

[display]
width = {display_data['display_width']}
height = {display_data['display_height']}
cell_height = {display_data['cell_width']} # Modifying this is unrecommended.
cell_width = {display_data['cell_height']} # Modifying this is unrecommended.

[gallery]
columns = 3
rows = 2

[gallery.controls]
forward = 'a'
backward = 'd'
select = 'e'

search = 's'
config = 'q'
return = 'x'

[reader]
# This will take longer as images go through Pillow
scale_to_width = false

# This will change the speed of image loading if scale_to_width is true
quality = 100

[reader.controls]
return = 'x'
forward = 'd'
backward = 'a'
'''

            with open(file=nhcli_configpath, mode='w', encoding='utf-8') as config_file:
                config_file.write(config_text)

            return config_text


def cli():
    # Initialize
    if nhcli_configpath.is_file() is False:
        config_text = nhclientai.Utilities.make_config()
        config = Config([config_text])

    else:
        config = Config(nhcli_configpath)

    nhcli = nhclientai(config)

    # Program
    action_map = {
        'home': nhcli.homepage,
        'search': nhcli.search,
        'view': nhcli.viewer,
        'config': nhcli.config
    }

    result = 'home'  # Show Homepage on Startup
    payload = None

    while True:
        result = action_map[result](payload)

        if result not in [key for key in action_map]:
            # This is accessed only if in homepage or search and user has
            # chosen a doujin to view, in which case a magic number is
            # returned instead of an action.
            result = nhcli.viewer(result)
