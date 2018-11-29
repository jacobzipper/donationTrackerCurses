from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import requests
import utils
import donations

class AddButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        name = inps[0][0].inputted
        shortDesc = inps[1][0].inputted
        desc = inps[2][0].inputted
        value = inps[3][0].inputted
        category = inps[4][0].inputted
        sess = utils.getSession()
        r = requests.post(API_URL + '/' + sess['role'] + '/adddonation', data = {'name': name, 'shortdescription': shortDesc, 'description': desc, 'value': value, 'category': category}, headers = {'Authorization': 'Bearer ' + sess['jwt']})
        js = r.json()
        if js['error'] != 0:
            return getScreen(stdscr)
        else:
            return donations.getScreen(stdscr)

class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return donations.getScreen(stdscr)

def getScreen(stdscr):
    return Screen(
        stdscr,
        8,
        4,
        [
            Text(1, 2, 'Register')
        ],
        [
            [TextInput(2, 2, "Name")],
            [TextInput(3, 2, "ShortDsc")],
            [TextInput(4, 2, "Desc")],
            [TextInput(5, 2, "Value")],
            [TextInput(6, 2, "Category")],
            [
                AddButton(7, 1, "Add"),
                BackButton(7, 3, "Back")
            ]
        ]
    )