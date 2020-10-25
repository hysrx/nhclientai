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
    def __init__(self, file_path):
        with open(filename=file_path, mode='r', encoding='utf-8') as config_file:
            config_data = toml.load(config_file)


class Downloader:
    pass
