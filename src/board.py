from constants import *
from sqaures import Square

class Board:

    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self._create()
        self._fenToBoard()

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row][col] = Square(row, col)

    def _fenToBoard(self, fenString=FEN): 
        fen = fenString.split(" ")
        rows = fen[0].split("/")

        for row in range(len(rows)):
            for col in range(len(rows[row])):
                # Is it a number?
                if rows[row][col].isdigit():
                    continue
                else:
                    fenCharacter = rows[row][col]
                    # Determine the colour
                    colour = "WHITE" if fenCharacter.isupper() else "BLACK"
                    # Create the piece
                    piece = FEN_MAPPING[fenCharacter.lower()](colour)
                    # Add the piece to the board
                    self.board[row][col].piece = piece


