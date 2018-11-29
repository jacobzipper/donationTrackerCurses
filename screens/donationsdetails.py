from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import utils
import requests
import search


class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return search.getScreen(stdscr)

def getScreen(stdscr, donation):
    don = {'name': 0, 'locationid': 1, 'tstamp': 2, 'shortdescription': 3, 'description': 4, 'comments': 5, 'value': 6, 'category': 7}
    txts = [Text(don[k] + 1, 1, ((k.upper() + ': ').ljust(20)) + str(donation[k]).ljust(50)) for k in donation.keys() if k in don]
    return Screen(
        stdscr,
        10,
        2,
        txts,
        [[BackButton(9, 1, "Back")]]
    )