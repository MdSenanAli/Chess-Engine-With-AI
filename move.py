class Move:
    def __init__(self, initial, final, piece=None) -> None:
        self.initial_tile = initial
        self.final_tile = final
        self.piece = piece
