import curses 
stdscr = curses.initscr()

grid_w, grid_h = stdscr.getmaxyx()
stdscr.addstr(1, 0, str(grid_w))
stdscr.addstr(2, 0, str(grid_h))
stdscr.refresh()