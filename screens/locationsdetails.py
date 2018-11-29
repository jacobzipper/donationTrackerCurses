from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import utils
import requests
import locations


class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return locations.getScreen(stdscr)

def getScreen(stdscr, location):
    loc = {'name': 0, 'type': 1, 'latitude': 2, 'longitude': 3, 'address': 4, 'phone': 5}
    txts = [Text(loc[k] + 1, 1, ((k.upper() + ': ').ljust(15)) + str(location[k]).ljust(50)) for k in location.keys() if k in loc]
    return Screen(
        stdscr,
        8,
        2,
        txts,
        [[BackButton(7, 1, "Back")]]
    )