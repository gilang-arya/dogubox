import curses

# init warna
def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)   # header
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # highlight
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)  # status bar
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)    # error/status

# gambar header
def draw_header(stdscr, text, margin_y=0, margin_x=0):
    stdscr.addstr(0 + margin_y, 3 + margin_x, text)

# gambar menu
def draw_menu(stdscr, items, selected_index, margin_y=0, margin_x=0):
    height, width = stdscr.getmaxyx()
    for idx, item in enumerate(items):
        row_y = 2 + idx + margin_y
        col_x = 1 + margin_x
        text = f"▸ {item}"
        if idx == selected_index:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(row_y, col_x, text.ljust(width - 3 - margin_x))
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.addstr(row_y, col_x, text)

# gambar status bar
def draw_status(stdscr, text, color_pair=3, margin_y=0, margin_x=0):
    height, width = stdscr.getmaxyx()
    stdscr.attron(curses.color_pair(color_pair))
    stdscr.addstr(height - 1 - margin_y, 1 + margin_x, text.ljust(width - 3 - margin_x))
    stdscr.attroff(curses.color_pair(color_pair))
