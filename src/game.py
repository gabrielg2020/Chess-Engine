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
                    
                
        