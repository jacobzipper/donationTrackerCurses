from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import requests
import welcome

class RegisterButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        username = inps[0][0].inputted
        password = inps[1][0].inputted
        firstname = inps[2][0].inputted
        lastname = inps[3][0].inputted
        role = inps[4][0].inputted
        r = requests.post(API_URL + '/registration', data = {'role': role, 'username': username, 'password': password, 'firstname': firstname, 'lastname': lastname})
        js = r.json()
        if js['error'] != 0:
            return getScreen(stdscr)
        else:
            return welcome.getScreen(stdscr)

class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return welcome.getScreen(stdscr)

def getScreen(stdscr):
    return Screen(
        stdscr,
        8,
        4,
        [
            Text(1, 2, 'Register')
        ],
        [
            [TextInput(2, 2, "Username")],
            [TextInput(3, 2, "Password")],
            [TextInput(4, 2, "First")],
            [TextInput(5, 2, "Last")],
            [TextInput(6, 2, "Role")],
            [
                RegisterButton(7, 1, "Register"),
                BackButton(7, 3, "Back")
            ]
        ]
    )