import curses
import subprocess
from model import MENU_ITEMS, COMMANDS
from keys import KEY_UP, KEY_DOWN, KEY_ENTER, KEY_QUIT
import ui

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.noecho()
    curses.cbreak()

    ui.init_colors()

    selected_index = 0
    status_text = "Use ↑ ↓ to move, Enter to run, q to quit"
    selected_command = None

    # ---- Margin ----
    margin_y, margin_x = 1, 3
    max_y, max_x = stdscr.getmaxyx()
    win = curses.newwin(
        max_y - 2*margin_y,
        max_x - 2*margin_x,
        margin_y,
        margin_x
    )
    win.keypad(True)

    while True:
        win.clear()
        win.border()  # border untuk menandai window dengan margin
        ui.draw_header(win, " NijiBox - Custom Script Toolbox ", margin_y=0, margin_x=2)
        ui.draw_menu(win, MENU_ITEMS, selected_index, margin_y=0, margin_x=1)
        ui.draw_status(win, status_text, color_pair=3, margin_y=0, margin_x=1)
        win.refresh()

        key = win.getch()
        if key == KEY_QUIT:
            break
        elif key == KEY_UP and selected_index > 0:
            selected_index -= 1
        elif key == KEY_DOWN and selected_index < len(MENU_ITEMS) - 1:
            selected_index += 1
        elif key in KEY_ENTER:
            current_item = MENU_ITEMS[selected_index]
            selected_command = COMMANDS.get(current_item)
            break

    return selected_command

if __name__ == "__main__":
    cmd_to_run = curses.wrapper(main)
    if cmd_to_run:
        print(f"Running: {' '.join(cmd_to_run)}\n")
        try:
            subprocess.run(cmd_to_run)
        except Exception as e:
            print(f"Error: {e}")
        print("\nPress Enter to exit...")
        input()
