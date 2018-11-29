import curses
import os

SCREEN_HEIGHT = 32
SCREEN_WIDTH = 135

def writeSession(js):
    open(os.environ.get('HOME') + '/.donationTrackerCursesSession', 'w').write('\n'.join([js['jwt'], js['firstname'], js['lastname'], js['role']]))

def getSession():
    lines = open(os.environ.get('HOME') + '/.donationTrackerCursesSession', 'r').read().split('\n')
    return {'jwt': lines[0], 'firstname': lines[1], 'lastname': lines[2], 'role': lines[3]}

def getY(row, nrows):
    return int((float(row) / nrows) * SCREEN_HEIGHT)

def getX(col, ncols, strn):
    return int((float(col) / ncols) * SCREEN_WIDTH) - (len(strn) / 2)

class Text():

    def __init__(self, row, col, strn):
        self.row = row
        self.col = col
        self.strn = strn

    def draw(self, stdscr, nrows, ncols):
        stdscr.addstr(getY(self.row, nrows), getX(self.col, ncols, self.strn), self.strn)

class Button():

    def __init__(self, row, col, strn):
        self.row = row
        self.col = col
        self.strn = strn

    def draw(self, stdscr, nrows, ncols, highlighted):
        stdscr.addstr(getY(self.row, nrows), getX(self.col, ncols, self.strn), self.strn, curses.A_REVERSE if highlighted else curses.A_UNDERLINE)

    def drawCursor(self, stdscr, nrows, ncols):
        stdscr.move(getY(self.row, nrows), getX(self.col, ncols, self.strn))

    def press(self, stdscr, inps):
        return None

class TextInput():

    def __init__(self, row, col, strn):
        self.row = row
        self.col = col
        self.strn = strn
        self.inputted = ''
        self.total = self.updateTotal()

    def updateTotal(self):
        return (self.strn + ': ').ljust(10) + self.inputted.ljust(50)

    def draw(self, stdscr, nrows, ncols, highlighted):
        self.total = self.updateTotal()
        stdscr.addstr(getY(self.row, nrows), getX(self.col, ncols, self.total), self.total, curses.A_REVERSE if highlighted else curses.A_UNDERLINE)

    def drawCursor(self, stdscr, nrows, ncols):
        stdscr.move(getY(self.row, nrows), getX(self.col, ncols, '') - 20 + len(self.inputted))

    def add(self, c):
        if len(self.inputted) < 50:
            self.inputted += chr(c)

    def remove(self):
        if len(self.inputted) > 0:
            self.inputted = self.inputted[:len(self.inputted) - 1]

class Screen():

    def __init__(self, stdscr, nrows, ncols, txts, inps):
        self.nrows = nrows
        self.ncols = ncols
        self.txts = txts
        self.inps = inps
        self.stdscr = stdscr
        self.curRow = 0
        self.curCol = 0

    def draw(self):
        for txt in self.txts:
            txt.draw(self.stdscr, self.nrows, self.ncols)

        for i in xrange(len(self.inps)):
            for j in xrange(len(self.inps[i])):
                self.inps[i][j].draw(self.stdscr, self.nrows, self.ncols, i == self.curRow and j == self.curCol)

        if len(self.inps) > 0:
            self.inps[self.curRow][self.curCol].drawCursor(self.stdscr, self.nrows, self.ncols)

        self.stdscr.refresh()

    def process(self, c):
        if c == curses.KEY_UP:
            self.curRow = (self.curRow - 1) % len(self.inps)
        elif c == curses.KEY_DOWN:
            self.curRow = (self.curRow + 1) % len(self.inps)
        elif c == curses.KEY_RIGHT:
            self.curCol = (self.curCol + 1) % len(self.inps[self.curRow])
        elif c == curses.KEY_LEFT:
            self.curCol = (self.curCol - 1) % len(self.inps[self.curRow])
        elif (c == curses.KEY_ENTER or c == 10 or c == 13) and isinstance(self.inps[self.curRow][self.curCol], Button):
            return self.inps[self.curRow][self.curCol].press(self.stdscr, self.inps)
        elif isinstance(self.inps[self.curRow][self.curCol], TextInput):
            if c > 31 and c < 127:
                self.inps[self.curRow][self.curCol].add(c)
            elif c == curses.KEY_BACKSPACE:
                self.inps[self.curRow][self.curCol].remove()
        elif c == 27:
            return None
        return self

