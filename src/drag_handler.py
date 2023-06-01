import pygame as py
from constants import *

class DragHandler:

    def __init__(self):
        self.dragging = False
        self.pieceSquarePos = (0, 0)
        self.mousePos = (0, 0)
        self.piece = None
        print(self.piece)

    # Render the piece being dragged
    def updateDragging(self, surface):
        # Get the image of the piece, the center of image = mouse position
        image = py.image.load(self.piece.image)
        imageCenter =  self.mousePos

        # Get the rect of the image
        self.piece.imageRect = image.get_rect(center=imageCenter)

        # Draw the image
        surface.blit(image, self.piece.imageRect)

    # Grab the mouse position
    def updateMousePos(self, pos):
        self.mousePos = pos

    # Save the pieces square position
    def updatePieceSquarePos(self, pos):
        # Convert the position to a square position
        row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
        self.pieceSquarePos = (row, col)

    # Save the piece being dragged
    def updatePiece(self, piece):
        self.piece = piece
        self.dragging = True

    # Remove the saved piece
    def removePiece(self):
        self.piece = None
        self.dragging = False
