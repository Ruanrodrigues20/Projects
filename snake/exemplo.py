# Exemplo p1 Computação@UFCG
# Dalton Serey (2022)
from curses import wrapper
import curses
import time
import random

QUIT = 113 # 'q'

def exemplo():
    contador = 0
    lin = random.randint(1, NLINS - 1)
    scr.addstr(lin, 0, "Oi! (Tecle q para sair!)")
    while True:
        key = scr.getch()
        if key == QUIT: break
        scr.addstr(0, 0, f"{contador}")
        contador += 1


scr, NLINS, NCOLS = None, 0, 0
def main(stdscr):
    global scr, NLINS, NCOLS
    curses.curs_set(0)
    stdscr.nodelay(True)
    scr = stdscr
    NLINS, NCOLS = stdscr.getmaxyx()
    exemplo()

wrapper(main)