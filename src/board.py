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
            col = 0
            for char in rows[row]:
                if char.isdigit():
                    for _ in range(int(char)): # create the correct number of empty squares
                        self.board[row][col].piece = None
                        col += 1
                else:
                    fenCharacter = char
                    # Determine the colour
                    colour = "WHITE" if fenCharacter.isupper() else "BLACK"
                    # Create the piece
                    piece = FEN_MAPPING[fenCharacter.lower()](colour)
                    # Add the piece to the board
                    self.board[row][col].piece = piece
                    col += 1

    def getMoves(self, square): # Will take a piece and return a list of moves
        self._generateMoves(square)
        # TODO: In future, this will return a list of moves that are legal

    def _generateMoves(self, square): # Will take a piece and generate pseudo-legal moves
        moves = []
        piece = square.piece
        # Get the row and column of the square the piece is on


        def _pawnMoves():
            # -- 1 Move Foward and 2 Moves Forward --
            # Make sure the move is on the board
            if square.row + piece.direction in range(ROWS):
                # Is there not a piece in front of the pawn?
                if not self.board[square.row + piece.direction][square.col].hasPiece():
                    # It can move forward
                    moves.append((square.row + piece.direction, square.col)) # 1↑

                    # Make sure the move is on the board
                    if square.row + piece.direction * 2 in range(ROWS):
                        # Has the pawn moved?
                        if not piece.moved:
                            # Can it move two squares?
                            if not self.board[square.row + piece.direction * 2][square.col].hasPiece():
                                moves.append((square.row + piece.direction * 2, square.col)) # 2↑

            # -- Diagonal Capture --
            # Make sure the move is on the board
            if square.row + piece.direction in range(ROWS) and square.col - 1 in range(COLS):
                # Is there a piece diagonally to the left of the pawn?
                if self.board[square.row + piece.direction][square.col - 1].hasPiece():
                    # Can it capture the piece?
                    if self.board[square.row + piece.direction][square.col - 1].piece.colour != piece.colour:
                        moves.append((square.row + piece.direction, square.col - 1))

            # Make sure the move is on the board
            if square.row + piece.direction in range(ROWS) and square.col + 1 in range(COLS):
                # Is there a piece diagonally to the right of the pawn?
                if self.board[square.row + piece.direction][square.col + 1].hasPiece():
                    # Can it capture the piece?
                    if self.board[square.row + piece.direction][square.col + 1].piece.colour != piece.colour:
                        moves.append((square.row + piece.direction, square.col + 1))



        def _knightMoves():
            pass

        def _bishopMoves():
            pass

        def _rookMoves():
            pass

        def _queenMoves():
            pass

        def _kingMoves():
            pass

        # Decides which function to call
        switch = {
            "pawn": _pawnMoves,
            "knight": _knightMoves,
            "bishop": _bishopMoves,
            "rook": _rookMoves,
            "queen": _queenMoves,
            "king": _kingMoves
        }

        # Call the function
        switch[piece.name]()

        # Set the moves
        piece.setMoves(moves)


    
       




