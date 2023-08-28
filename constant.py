# Defining the width and height of the pygame screen
WIDTH = 800
HEIGHT = 800

# Defining the number of rows and columns
ROWS = 8
COLS = 8

# Defining width of a tile
SQUARE = HEIGHT//ROWS

# For facing location for the board W vs B or B vs W
# (My piece: (pawn row, piece row),Enemy Piece: (pawn row, piece row))
PLAY_WHITE = ((6,7),(1,0))
PLAY_BLACK = ((1,0),(6,7))