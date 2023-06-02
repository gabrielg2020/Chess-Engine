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
        board = self.game.board
        screen = self.screen
        dragHandler = self.game.dragHandler

        # Game Loop
        while True:
            # Render the background, pieces and highlights
            game.renderBackground(screen)
            game.renderPieces(screen)
            game.renderHighlights(screen)
            # Render the piece being dragged
            if dragHandler.dragging:
                dragHandler.updateDragging(screen)
    
            for event in py.event.get():

                if event.type == py.MOUSEBUTTONDOWN and event.button == 1: # Mouse button pressed
                    dragHandler.updateMousePos(event.pos)
                    # Convert the mouse position to a square position
                    row, col = event.pos[1] // SQUARE_SIZE, event.pos[0] // SQUARE_SIZE

                    # Does the square have a piece?
                    if board.board[row][col].hasPiece():
                        # Save the piece
                        piece = board.board[row][col].piece
                        board.getMoves(board.board[row][col])
                        dragHandler.updatePieceSquarePos(event.pos)
                        dragHandler.updatePiece(piece)

                elif event.type == py.MOUSEMOTION: # Mouse moved
                    # Are we dragging a piece?
                    if dragHandler.dragging:
                        dragHandler.updateMousePos(event.pos)
                        
                elif event.type == py.MOUSEBUTTONUP and event.button == 1: # Mouse button released
                    dragHandler.removePiece()

                elif event.type == py.QUIT: # Quit the game
                    py.quit()
                    sys.exit()

            py.display.update()

main = Main()
main.run()
