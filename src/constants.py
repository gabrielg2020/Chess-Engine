from piece import *

# Rows and Columns of the board
ROWS = 8
COLS = 8
# Square size
SQUARE_SIZE = 100

# Width and Height of the window
WIDTH = COLS * SQUARE_SIZE
HEIGHT = ROWS * SQUARE_SIZE

# Colours for the board
COLOURS = {"GREEN": (122,150, 87), 
            "CREAM": (238,238,210),
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
