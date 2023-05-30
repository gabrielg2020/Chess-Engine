import pygame as py

from constants import *
from board import Board

class Game:

    def __init__(self):
        self.board = Board()

    def renderBackground(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                colour = COLOURS["CREAM"] if (row + col) % 2 == 0 else COLOURS["GREEN"]
                rect = py.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                py.draw.rect(screen, colour, rect)
                py.draw.rect(screen, (0,0,0), rect, 1)

                # Draw the letters and numbers
                textColour = COLOURS["GREEN"] if colour == COLOURS["CREAM"] else COLOURS["CREAM"]
                font = py.font.SysFont("Consolas", 20)

                # Numbers
                if col == 0:
                    number = font.render(str(8- row), True, textColour)
                    screen.blit(number, (col * SQUARE_SIZE + 5, row * SQUARE_SIZE + 5))

                # Letters
                if row == 7:
                    letter = font.render(chr(col + 97), True, textColour)
                    screen.blit(letter, (col * SQUARE_SIZE + 80, row * SQUARE_SIZE + 80))



    def renderPieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.board[row][col]
                if square.hasPiece():
                    piece = square.piece
                    # Get the image, center and rect
                    image = py.image.load(piece.image)
                    imageCenter = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    pieceRect = image.get_rect(center=imageCenter)
                    # Draw the image
                    screen.blit(image, pieceRect)
                    
                
        