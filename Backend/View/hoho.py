
import curses
def hello_world():
    # Initialize the curses library
    stdscr = curses.initscr()
    
    # Disable character echoing and enable special keys like function keys and arrow keys
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    # Print the initial prompt
    stdscr.addstr("Press any key to say Hello World")
    
    # Wait for user input
    stdscr.getch()
    
    # Clear the screen and print the final message
    stdscr.clear()
    stdscr.addstr("Hello World")
    
    # Refresh the screen to update the display
    stdscr.refresh()
    
    # Wait for another keypress before exiting
    stdscr.getch()
    
    # Restore the terminal to its original state
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# Call the function to run the program
hello_world()