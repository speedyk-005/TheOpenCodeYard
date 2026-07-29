"""Undo/redo playground using LifoQueue."""

import time
from queue import LifoQueue, Empty

history = LifoQueue()
undo_stack = LifoQueue(5)  # max size is 5 for undo operations


def do(action):
    history.put(action)  # Add action to history
    print(f"Action(s) done:  {history.qsize()} \n")


def undo():
    try:
        last_done_action = history.get_nowait()  # Get the last action
        undo_stack.put(last_done_action)  # Store in undo stack
        print(f"Undo {last_done_action}. Actions left: {history.qsize()} \n")
    except Empty:
        print("No actions to undo.")


def redo():
    try:
        last_undone_action = undo_stack.get_nowait()  # Get last undone action
        history.put(last_undone_action)  # Put it back in history
        print(f"Redo {last_undone_action}. Actions now: {history.qsize()} \n")
    except Empty:
        print("No actions to redo.")


if __name__ == "__main__":
    print("YOU CAN DO, UNDO OR REDO SOMETHING. \nnote: it is a playground.\n")
    print(" Commands : do('action'), undo(), redo(), exit() \n")

    while True:
        try:
            comd = input("> ").lower().strip()
            if comd.startswith("do(") and comd.endswith(")"):
                action = comd[3:-1]
                if action.strip():
                    do(action)
                else:
                    print("Invalid action. Action cannot be empty.\n")
            elif comd == "undo()":
                undo()
            elif comd == "redo()":
                redo()
            elif comd == "exit()":
                print("Exiting the playground...")
                time.sleep(1)
                print("Task done.")
                break
            else:
                print("Invalid command.\n")
        except:
            print("An error occurred. Please retry with the right command syntax.")