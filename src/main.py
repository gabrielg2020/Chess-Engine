import pygame as py
import sys

from src.constants import *

class Main:

    def __init__(self):
        # Pygame Setup
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption("Chess by @gabriel2020")


    def run(self):
        # Game Loop
        while True:
            for event in py.event.get():
                if event.type == py.QUIT: # Quit the game
                    py.quit()
                    sys.exit()

            py.display.update()

main = Main()
main.run()
