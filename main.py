import curses

from screens import welcome

from curses import wrapper

def main(stdscr):
    curScreen = welcome.getScreen(stdscr)
    while 1:
        curScreen.draw()
        c = stdscr.getch()
        curScreen = curScreen.process(c)
        if curScreen == None:
            break

wrapper(main)