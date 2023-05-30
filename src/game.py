import pygame as py

from constants import *

class Game:

    def __init__(self):
        pass

    def renderBackground(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                colour = COLOURS["CREAM"] if (row + col) % 2 == 0 else COLOURS["GREEN"]
                rect = py.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                py.draw.rect(screen, colour, rect)
        