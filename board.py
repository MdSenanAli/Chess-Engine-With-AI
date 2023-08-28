import itertools
from constant import *
from piece import *
from image import Image

# This class manages the board and related properties of the board
class Board:
    def __init__(self) -> None:
        # Initialize the game board as a 2D list with None values
        self.game_board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
        # List of piece classes and their corresponding types
        self.pcs_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook, Pawn]
        self.pcs_type = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook', 'pawn']

        # Initialize the image set and obtain the image dictionary
        self.image_set = Image("standard")
        self.images = self.image_set.image_dictionary()
        
        # Initialize the board by placing pieces in their starting positions
        self.initialise_board()

    # This function initializes the chessboard by placing pawns and non-pawn pieces
    # in their starting positions for both white and black players.
    def initialise_board(self) -> None:
        colors = ['white', 'black']
        
        for color, col in itertools.product(colors, range(COLS)):
            # Determine the starting row for pawns and non-pawn pieces based on color
            loc_pawn, loc_piece = (6, 7) if color == 'white' else (1, 0)
            
            # Initialize pawn and non-pawn pieces for the current color and column
            # Pawn initialization
            self.game_board[loc_pawn][col] = self.pcs_class[8](
                color, self.images[f"{color}-{self.pcs_type[8]}"]
            )
            
            # Non-pawn piece initialization (using col as index for the piece class)
            self.game_board[loc_piece][col] = self.pcs_class[col](
                color, self.images[f"{color}-{self.pcs_type[col]}"]
            )
  
  
    def rotate_board(self):
        for row in range(ROWS):
            self.game_board[row] = list(reversed(self.game_board[row]))
        self.game_board = list(reversed(self.game_board))