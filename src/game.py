import pygame as py

from constants import *
from board import Board
from drag_handler import DragHandler

class Game:

    def __init__(self):
        self.board = Board()
        self.dragHandler = DragHandler()
        self.boardSurface = py.Surface((WIDTH, HEIGHT))
        self._createBackground(self.boardSurface)

    def _createBackground(self, surface):
        # Get the colours from the board theme
        colours = BOARD_THEMES[BOARD_THEME]
        for row in range(ROWS):
            for col in range(COLS):
                colour = colours[1] if (row + col) % 2 == 0 else colours[0]
                rect = py.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                py.draw.rect(surface, colour, rect)
                py.draw.rect(surface, colours[2], rect, 1)

                # Draw the letters and numbers
                textColour = colours[0] if colour == colours[1] else colours[1]
                font = py.font.SysFont("Consolas", 20)

                # Numbers
                if col == 0:
                    number = font.render(str(8- row), True, textColour)
                    surface.blit(number, (col * SQUARE_SIZE + 5, row * SQUARE_SIZE + 5))

                # Letters
                if row == 7:
                    letter = font.render(chr(col + 97), True, textColour)
                    surface.blit(letter, (col * SQUARE_SIZE + 80, row * SQUARE_SIZE + 80))

    def renderBackground(self, screen):
        screen.blit(self.boardSurface, (0, 0))

    def renderPieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.board[row][col]
                # Does the square have a piece?
                if square.hasPiece():
                    piece = square.piece

                    # Are we not dragging the piece?
                    if piece is not self.dragHandler.piece: # Will removes the piece form board whilst dragging
                        # Get the image, center and rect
                        image = py.image.load(piece.image)
                        imageCenter = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                        pieceRect = image.get_rect(center=imageCenter)
                        # Draw the image
                        screen.blit(image, pieceRect)

    def renderHighlights(self, screen):
        # Hightlight possible moves
        highlightedSquares = self.board.highlightedSquares
        for square in highlightedSquares:
            row, col = square
            surface = py.Surface((SQUARE_SIZE, SQUARE_SIZE), py.SRCALPHA)
            # If the square has a piece, large circle else dot
            if self.board.board[row][col].hasPiece():
                py.draw.circle(surface, HIGHLIGHT_MOVE, (SQUARE_SIZE // 2, SQUARE_SIZE // 2), SQUARE_SIZE // 2, 7)
            else:
                py.draw.circle(surface, HIGHLIGHT_MOVE, (SQUARE_SIZE // 2, SQUARE_SIZE // 2), 15)

            screen.blit(surface, (col * SQUARE_SIZE, row * SQUARE_SIZE))

        # Highlight previous move
        if self.board.previousMove:
            fromSquare, toSquare = self.board.previousMove
            fromRow = fromSquare.row
            fromCol = fromSquare.col
            toRow = toSquare.row
            toCol = toSquare.col
            surface = py.Surface((SQUARE_SIZE, SQUARE_SIZE), py.SRCALPHA)
            py.draw.rect(surface, PREVIOUS_MOVE, (0, 0, SQUARE_SIZE, SQUARE_SIZE), 7)
            screen.blit(surface, (fromCol * SQUARE_SIZE, fromRow * SQUARE_SIZE))
            screen.blit(surface, (toCol * SQUARE_SIZE, toRow * SQUARE_SIZE))

        # Highlight Selected square
        if self.board.selectedSquare:
            row = self.board.selectedSquare.row
            col = self.board.selectedSquare.col
            surface = py.Surface((SQUARE_SIZE, SQUARE_SIZE), py.SRCALPHA)
            py.draw.rect(surface, SELECTED, (0, 0, SQUARE_SIZE, SQUARE_SIZE), 7)
            screen.blit(surface, (col * SQUARE_SIZE, row * SQUARE_SIZE))

                    
                
        