class Piece:
    def __init__(self, color, points, image) -> None:
        self.color = color
        self.points = points
        self.image = image
        self.name = None
        self.dragged = False


class Pawn(Piece):
    def __init__(self, color, image) -> None:
        points = 1 if color == "white" else -1
        super().__init__(color, points, image)

        self.name = f"{color}-pawn"


class Rook(Piece):
    def __init__(self, color, image) -> None:
        points = 5 if color == "white" else -5
        super().__init__(color, points, image)

        self.name = f"{color}-rook"


class Bishop(Piece):
    def __init__(self, color, image) -> None:
        points = 3 if color == "white" else -3
        super().__init__(color, points, image)

        self.name = f"{color}-bishop"


class Knight(Piece):
    def __init__(self, color, image) -> None:
        points = 3 if color == "white" else -3
        super().__init__(color, points, image)

        self.name = f"{color}-knight"


class Queen(Piece):
    def __init__(self, color, image) -> None:
        points = 9 if color == "white" else -9
        super().__init__(color, points, image)

        self.name = f"{color}-queen"


class King(Piece):
    def __init__(self, color, image) -> None:
        points = 1000 if color == "white" else -1000
        super().__init__(color, points, image)

        self.name = f"{color}-king"
