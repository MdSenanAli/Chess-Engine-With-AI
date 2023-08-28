from constant import *


class Board:
    def __init__(self) -> None:
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]