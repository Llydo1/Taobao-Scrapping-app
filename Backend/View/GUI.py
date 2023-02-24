import sys
import tty
import termios
import os, time

def option1():
    global result
    result += "Option 1 selected\n"
    print(result)

def option2():
    global result
    result += "Option 2 selected\n"
    print(result)

def option3():
    global result
    result += "Option 3 selected\n"
    print(result)

def option4():
    global result
    result += "Option 4 selected\n"
    print(result)

result = ""
current_choice = 1

def get_key():
    """
    Get a single character from the user without requiring them to press enter.
    """
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return ch
print("Choose an option:")
while True:
    

    if current_choice == 1:
        print("\033[7m1. Option 1\033[0m")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
    elif current_choice == 2:
        print("1. Option 1")
        print("\033[7m2. Option 2\033[0m")
        print("3. Option 3")
        print("4. Option 4")
    elif current_choice == 3:
        print("1. Option 1")
        print("2. Option 2")
        print("\033[7m3. Option 3\033[0m")
        print("4. Option 4")
    elif current_choice == 4:
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("\033[7m4. Option 4\033[0m")

    choice = None
    while choice is None:
        key = get_key()
        if key == "\033":
            # Arrow key was pressed
            print("hehe")
            key = get_key()
            if key == "[":
                # Arrow key sequence continues
                key = get_key()
                if key == "A":
                    # Up arrow key
                    current_choice = max(current_choice - 1, 1)
                elif key == "B":
                    # Down arrow key
                    current_choice = min(current_choice + 1, 4)
        elif key == "\r":
            # Enter key
            choice = str(current_choice)
            print("hehehe")
        print(key)
        break

    if choice == "1":
        print("hehe")
        option1()
        time.sleep(5)
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        break

