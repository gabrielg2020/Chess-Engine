import pygame as py

from constants import *
from board import Board

class Game:

    def __init__(self):
        self.board = Board()

    def renderBackground(self, screen):
        # Get the colours from the board theme
        colours = BOARD_THEMES[BOARD_THEME]
        for row in range(ROWS):
            for col in range(COLS):
                colour = colours[1] if (row + col) % 2 == 0 else colours[0]
                rect = py.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                py.draw.rect(screen, colour, rect)
                py.draw.rect(screen, colours[2], rect, 1)

                # Draw the letters and numbers
                textColour = colours[0] if colour == colours[1] else colours[1]
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
                    
                
        