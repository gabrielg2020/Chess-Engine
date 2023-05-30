import pygame as py
import sys

from constants import *
from game import Game

class Main:

    def __init__(self):
        # Pygame Setup
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption("Chess by @gabriel2020")

        self.game = Game()

    def run(self):
        game = self.game
        screen = self.screen
        # Game Loop
        while True:
            game.renderBackground(screen)
            game.renderPieces(screen)
            for event in py.event.get():
                if event.type == py.QUIT: # Quit the game
                    py.quit()
                    sys.exit()

            py.display.update()

main = Main()
main.run()
