from utils import Text, Button, TextInput, Screen

import login
import register

class LoginButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return login.getScreen(stdscr)

class RegisterButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return register.getScreen(stdscr)

def getScreen(stdscr):
    return Screen(
        stdscr,
        3,
        4,
        [
            Text(1, 2, 'Welcome to Donation Tracker')
        ],
        [
            [
                LoginButton(2, 1, "Login"),
                RegisterButton(2, 3, "Register")
            ]
        ]
    )