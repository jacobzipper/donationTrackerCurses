from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import utils
import requests
import welcome
import locations

class LoginButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()

        username = inps[0][0].inputted
        password = inps[1][0].inputted

        r = requests.post(API_URL + '/login', data = {'username': username, 'password': password})
        js = r.json()
        if js['error'] != 0:
            return getScreen(stdscr)
        else:
            utils.writeSession(js)
            return locations.getScreen(stdscr)


class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return welcome.getScreen(stdscr)

def getScreen(stdscr):
    return Screen(
        stdscr,
        5,
        4,
        [
            Text(1, 2, 'Login')
        ],
        [
            [TextInput(2, 2, "Username")],
            [TextInput(3, 2, "Password")],
            [
                LoginButton(4, 1, "Login"),
                BackButton(4, 3, "Back")
            ]
        ]
    )