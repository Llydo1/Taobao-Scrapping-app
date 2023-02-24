import curses
import sys
sys.path.insert(0, '..')
from Controller.product_controller import ProductController
from Controller.store_controller import StoreController
import time

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Exit"]
selected_option = 0

def display_options(stdscr):
    stdscr.clear()
    for i, option in enumerate(options):
        prefix = "> " if i == selected_option else "  "
        stdscr.addstr(i, 0, prefix + option)
    stdscr.addstr("\n")
    stdscr.refresh()

def select_option(stdscr):
    global selected_option
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(options)
        elif key == ord('\n'):
            selected = options[selected_option]
            if selected == "Exit":
                return False
            option_controller(stdscr,selected)
            stdscr.addstr(len(options) + 1, 0, "Selected option: " + selected)
            stdscr.refresh()
            stdscr.getch()
        display_options(stdscr)

def option_controller(stdscr, selected):
    store_controller = StoreController(stdscr)
    stdscr.addstr("\nbinbin")
    time.sleep(1)
    store_controller.scrap_store()


def main(stdscr):
    curses.curs_set(0)
    while True:
        display_options(stdscr)
        if not select_option(stdscr):
            break

curses.wrapper(main)
