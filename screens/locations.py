from utils import Text, Button, TextInput, Screen
from __init__ import API_URL

import utils
import requests
import welcome
import locationsdetails
import donations
import webbrowser

GMAPS_FORMAT = 'https://www.google.com/maps/dir/?api=1&origin=%s&destination=%s&travelmode=driving&waypoints=%s'

class LocationButton(Button):

    def __init__(self, row, col, strn, location):
        Button.__init__(self, row, col, strn)
        self.location = location

    def press(self, stdscr, inps):
        stdscr.clear()
        return locationsdetails.getScreen(stdscr, self.location)

class DonationsButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return donations.getScreen(stdscr)

class MapButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        r = requests.get(API_URL + '/locations')
        js = r.json()
        locs = map(lambda x: x['address'], js['locations'])
        origin = locs.pop(0)
        dest = locs.pop()
        waypoints = '|'.join(locs)
        url = GMAPS_FORMAT % (origin, dest, waypoints)
        webbrowser.open(url)
        return getScreen(stdscr)

class BackButton(Button):

    def press(self, stdscr, inps):
        stdscr.clear()
        return welcome.getScreen(stdscr)

def getScreen(stdscr):
    r = requests.get(API_URL + '/locations')
    js = r.json()
    rows = len(js['locations']) + 4
    locations = [[LocationButton(i + 2, 2, js['locations'][i]['name'], js['locations'][i])] for i in range(len(js['locations']))]
    locations += [[DonationsButton(rows - 1, 1, "Donations"), MapButton(rows - 1, 2, "Map"), BackButton(rows - 1, 3, "Back")]]

    sess = utils.getSession()
    return Screen(
        stdscr,
        rows,
        4,
        [
            Text(1, 2, 'Welcome %s %s you are a %s.' % (sess['firstname'], sess['lastname'], sess['role'][:len(sess['role']) - 1]))
        ],
        locations
    )