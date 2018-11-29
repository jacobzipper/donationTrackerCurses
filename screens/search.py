from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import requests
import utils
import donations
import searchresults

class SearchResultsButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        category = inps[0][0].inputted
        name = inps[1][0].inputted
        sess = utils.getSession()
        r = requests.get(API_URL + '/' + sess['role'] + '/searchdonations', params = {'category': category, 'name': name}, headers = {'Authorization': 'Bearer ' + sess['jwt']})
        js = r.json()
        return searchresults.getScreen(stdscr, js['donations'])

class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return donations.getScreen(stdscr)

def getScreen(stdscr):
    return Screen(
        stdscr,
        5,
        4,
        [
            Text(1, 2, 'Search')
        ],
        [
            [TextInput(2, 2, "Category")],
            [TextInput(3, 2, "Name")],
            [
                SearchResultsButton(4, 1, "Search"),
                BackButton(4, 3, "Back")
            ]
        ]
    )