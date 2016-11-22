from sys import argv


SHEET = "Sheet 1"


def start_day():
    # Post date and time to sheet
    # Save date and time to cache
    pass


def end_day():
    # Calculate time spent
    # Post end-time to sheet
    # Post time to sheet
    pass


def main():
    for arg in argv:
        if arg == "start":
            start_day()
        elif arg == "end":
            end_day()

if __name__ == '__main__':
    main()