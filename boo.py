import curses
import random
from get_data import *

def get_fortune(stdscr):
    stdscr.addstr(0, 0, "# Source fortune quotes: https://github.com/bmc/fortunes.git")
    return random.choice(fortune_leaves)

def get_tarot(stdscr):
    random_card_key = random.choice(list(tarot_cards.keys()))
    random_card = tarot_cards[random_card_key]

    stdscr.addstr("# Source: https://lizdean.info/wp-content/uploads/2018/01/Tarot-Card-Meanings.pdf")
    stdscr.addstr(2, 0, "{}".format(random_card['Name']))

    # Displaying multi-line description
    description_lines = random_card['Description'].split('\n')
    for i, line in enumerate(description_lines, start=3):
        stdscr.addstr(i, 0, line)

def greetings(stdscr):
    stdscr.border()

    height, width = stdscr.getmaxyx()

        # Display text with all lines centered vertically
    lines = [
        "Hi there, I'm boo",
        "What can I do for you today?",
        "1. Get a fortune cookie",
        "2. Get a tarot card",
        "3. Exit",
        "Select: "
    ]

    for i, line in enumerate(lines):
        line_x = max(0, (width - len(line)) // 2)
        line_y = max(0, (height - len(lines)) // 2) + i
        stdscr.addstr(line_y, line_x, line, curses.A_BOLD)

def end(stdscr):
    stdscr.border()

    height, width = stdscr.getmaxyx()

    # Display text with all lines centered vertically
    lines = [
        "Goodbye!",
        "Have a nice day •ᴗ•"
    ]

    for i, line in enumerate(lines):
        line_x = max(0, (width - len(line)) // 2)
        line_y = max(0, (height - len(lines)) // 2) + i
        stdscr.addstr(line_y, line_x, line, curses.A_BOLD)

def main(stdscr):
    while True:
        stdscr.clear()
        greetings(stdscr)
        stdscr.refresh()

        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.clear()
            stdscr.addstr(2, 0, "Your fortune is:")
            stdscr.addstr(3, 0, get_fortune(stdscr))
            stdscr.refresh()
            stdscr.getch()
        
        elif choice == ord('2'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Okay, let's take a deep breath")
            stdscr.addstr(2, 0, "Press any key to draw a card")
            stdscr.getch()
            stdscr.clear()
            get_tarot(stdscr)
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('3'):
            stdscr.clear()
            end(stdscr)
            stdscr.refresh()
            stdscr.getch()
            break

        else:
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
