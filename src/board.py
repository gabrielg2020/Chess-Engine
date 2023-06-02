from constants import *
from sqaures import Square

class Board:

    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.highlightedSquares = []
        self.previousMove = None
        self.selectedSquare = None
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
                    colour = "white" if fenCharacter.isupper() else "black"
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
        # Get the piece's direction, row and col
        direction = piece.direction
        row = square.row
        col = square.col

        def _generateSlidingMoves(offsets): # This function will only be called by: _rookMoves, _bishopMoves, _queenMoves
            # For each offset, check if the move is on the board
            for offset in offsets:
                for i in range(1, ROWS):
                    # Calculate new row and col
                    newRow = row + offset[0] * i
                    newCol = col + offset[1] * i

                    # If the move is not on the board, break
                    if newRow not in range(ROWS) or newCol not in range(COLS):
                        break

                    # If there is a piece of the same colour, break
                    if self.board[newRow][newCol].hasPiece() and self.board[newRow][newCol].piece.colour == piece.colour:
                        break

                    # If there is a piece of the opposite colour, add the move and break
                    if self.board[newRow][newCol].hasPiece() and self.board[newRow][newCol].piece.colour != piece.colour:
                        moves.append((newRow, newCol))
                        break

                    # If there is no piece, add the move
                    if not self.board[newRow][newCol].hasPiece():
                        moves.append((newRow, newCol))

        def _generateDirectionalMoves(directions): # This function will only be called by: _knightMoves, _kingMoves
            # For each direction, check if the move is on the board
            for direction in directions:
                # Calculate new row and col
                newRow = row + direction[0]
                newCol = col + direction[1]
                # Make sure the move is on the board
                if newRow in range(ROWS) and newCol in range(COLS):
                    # Make sure there is not a piece of the same colour
                    if not self.board[newRow][newCol].hasPiece() or self.board[newRow][newCol].piece.colour != piece.colour:
                            moves.append((newRow, newCol))

        def _pawnMoves():
            # -- 1 Move Foward and 2 Moves Forward --
            # Make sure the move is on the board
            if row + direction in range(ROWS):
                # Is there not a piece in front of the pawn?
                if not self.board[row + direction][col].hasPiece():
                    # It can move forward
                    moves.append((row + direction, col)) # 1↑

                    # Make sure the move is on the board
                    if row + direction * 2 in range(ROWS):
                        # Has the pawn moved?
                        if not piece.moved:
                            # Can it move two squares?
                            if not self.board[row + direction * 2][col].hasPiece():
                                moves.append((row + direction * 2, col)) # 2↑

            # -- Diagonal Capture --
            # Make sure the move is on the board
            if row + direction in range(ROWS) and col - 1 in range(COLS):
                # Is there a piece diagonally to the left of the pawn?
                if self.board[row + direction][col - 1].hasPiece():
                    # Can it capture the piece?
                    if self.board[row + direction][col - 1].piece.colour != piece.colour:
                        moves.append((row + direction, col - 1))

            # Make sure the move is on the board
            if row + direction in range(ROWS) and col + 1 in range(COLS):
                # Is there a piece diagonally to the right of the pawn?
                if self.board[row + direction][col + 1].hasPiece():
                    # Can it capture the piece?
                    if self.board[row + direction][col + 1].piece.colour != piece.colour:
                        moves.append((row + direction, col + 1))

        def _knightMoves():
            # Move directions
            directions = [(2, 1),(2, -1),(1, 2),(1, -2),(-2, 1),(-2, -1),(-1, 2),(-1, -2),]
            _generateDirectionalMoves(directions)
            
        def _bishopMoves():
            # Move offsets
            offsets = [(direction, -1), (direction, 1), (-direction, -1), (-direction, 1)]
            _generateSlidingMoves(offsets)
            

        def _rookMoves():
            # Move offsets
            offsets = [(direction, 0), (-direction, 0), (0, -1), (0, 1)]
            _generateSlidingMoves(offsets)

        def _queenMoves():
            #Move offsets
            offsets = [(direction, -1), (direction, 1), (-direction, -1), (-direction, 1), (direction, 0), (-direction, 0), (0, -1), (0, 1)]
            _generateSlidingMoves(offsets)

        def _kingMoves():
            # Move directions
            directions = [(1, 0),(-1, 0),(0, 1),(0, -1),(1, 1),(1, -1),(-1, 1),(-1, -1)]
            _generateDirectionalMoves(directions)

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
        # Save moves to highlighted squares
        self.highlightedSquares = moves

    def movePiece (self, fromSquare, toSquare):
        toSquare.piece = fromSquare.piece
        fromSquare.piece = None

        # Store move
        self.previousMove = (fromSquare, toSquare)