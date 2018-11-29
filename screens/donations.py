from utils import Text, Button, TextInput, Screen

import search
import add
import locations
import utils

class SearchButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return search.getScreen(stdscr)

class AddButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return add.getScreen(stdscr)

class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return locations.getScreen(stdscr)

def getScreen(stdscr):
    sess = utils.getSession()
    inps = [SearchButton(2, 1, "Search"), AddButton(2, 2, "Add"), BackButton(2, 3, "Back")] if sess['role'] == 'employees' or sess['role'] == 'managers' else [SearchButton(2, 1, "Search"), BackButton(2, 3, "Back")]
    return Screen(
        stdscr,
        3,
        4,
        [
            Text(1, 2, 'Would you like to add or search for donations?')
        ],
        [
            inps
        ]
    )