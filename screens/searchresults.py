from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import utils
import requests
import search
import donationsdetails

class DonationButton(Button):

    def __init__(self, row, col, strn, donation):
        Button.__init__(self, row, col, strn)
        self.donation = donation

    def press(self, stdscr, inps):
        stdscr.clear()
        return donationsdetails.getScreen(stdscr, self.donation)

class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return search.getScreen(stdscr)

def getScreen(stdscr, donations):
    rows = len(donations) + 3
    donations = [[DonationButton(i + 2, 1, donations[i]['name'], donations[i])] for i in range(len(donations))]
    donations += [[BackButton(rows - 1, 1, "Back")]]

    sess = utils.getSession()
    return Screen(
        stdscr,
        rows,
        4,
        [],
        donations
    )