"""Button with auto-timeout using a daemon thread."""

import threading
from datetime import datetime, timedelta
import time


class Button:
    def __init__(self):
        self.state = False
        self.last_pressed = datetime.now()

    def press(self):
        self.state = True if self.state is False else False
        self.last_pressed = datetime.now()


button = Button()


def timeout():
    """Auto-reset button state after 3 seconds of inactivity."""
    while True:
        now = datetime.now()
        if (now - button.last_pressed) >= timedelta(seconds=3):
            if button.state:
                button.state = False
                print("\r Button resets automatically (disabled)." +
                      "\nYour command: ", end="")
            button.last_pressed = datetime.now()
        time.sleep(1)


time_out = threading.Thread(target=timeout, daemon=True)


def print_button_state():
    print("Button enabled.\n" if button.state else "Button disabled.\n")


def main():
    print("Auto timeout is set.")
    time_out.start()
    print("Write p for press or q to quit.\n")

    while (usr_inp := input("Your command: ").lower()) != "q":
        if usr_inp == "p":
            button.press()
            print_button_state()
        else:
            print("Wrong command.")
            print("Supported commands: p for press or q to quit.")


if __name__ == "__main__":
    main()