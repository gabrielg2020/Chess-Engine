from piece import *

# Rows and Columns of the board
ROWS = 8
COLS = 8
# Square size
SQUARE_SIZE = 100

# Width and Height of the window
WIDTH = COLS * SQUARE_SIZE
HEIGHT = ROWS * SQUARE_SIZE

# Board Theme Chosen # NOTE: This is not implemented yet naturally
BOARD_THEME = "CHECKERS"
# Board Themes for the board # STRUCTURE: (Colour 1, Colour 2, Outline Colour)
BOARD_THEMES = {"ORIGINAL": ((122,150, 87),(238,238,210), (0,0,0)),
                "BLUE": ((81,116,153),(234,233,210),(0,0,0)),
                "BROWN": ((176,134,100),(237,216,181),(0,0,0)),
                "BUBBLEGUM": ((248,215,221),(255,255,255),(0,0,0)),
                "CHECKERS": ((48,48,48),(190,72,82),(236,214,135)),
}

# FEN and FEN Mapping
FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
FEN_MAPPING = {
    "r": Rook,
    "n": Knight,
    "b": Bishop,
    "q": Queen,
    "k": King,
    "p": Pawn,
}
