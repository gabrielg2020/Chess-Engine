import os

class Piece:

    def __init__(self, name, colour, image=None, imageRect=None):
        self.name = name
        self.colour = colour
        self.moves = []
        self.moved = False

        # Piece image
        self.image = image
        self.setImage(80)
        self.imageRect = imageRect

    def setImage(self, size):
        # Path to image
        path = f"assets/images/{size}px/{self.colour}_{self.name}.png"
        self.image = os.path.join(path)


'''
All of the pieces below inherit from the Piece class.
'''
class Pawn(Piece):

    def __init__(self, colour):
        self.direction = 1 if colour == "white" else -1
        super().__init__("pawn", colour)

class Knight(Piece):

    def __init__(self, colour):
        self.direction = 1 if colour == "white" else -1
        super().__init__("knight", colour)

class Bishop(Piece):
    
    def __init__(self, colour):
        self.direction = 1 if colour == "white" else -1
        super().__init__("bishop", colour)

class Rook(Piece):
        
     def __init__(self, colour):
        self.direction = 1 if colour == "white" else -1
        super().__init__("rook", colour)

class Queen(Piece):

    def __init__(self, colour):
        self.direction = 1 if colour == "white" else -1
        super().__init__("queen", colour)

class King(Piece):

    def __init__(self, colour):
        self.direction = 1 if colour == "white" else -1
        super().__init__("king", colour)


    