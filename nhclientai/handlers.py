'''
nhclientai.handlers
===================
Licensed under the GPL v3 license, located in the LICENSE file included with the software.

by hysrx and nhclientai's contributors.
'''

from codecs import open

import toml
import os


class Input:
    pass


class Config:
    def __init__(self, argument):
        if isinstance(argument, list):
            # nhclientai.nhclientai.Utilities.make_config
            # was used so config_data was made on the spot
            self.data = toml.loads(argument[0])

        else:
            with open(filename=argument, mode='r', encoding='utf-8') as config_file:
                config_data = toml.load(config_file)

        self.data = argument

class Downloader:
    pass
