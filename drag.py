from image import Image
from constant import *
import math


class Drag:
    def __init__(self) -> None:
        # Initialize drag attributes
        self.x = None
        self.y = None
        self.initial_x = None
        self.initial_y = None
        self.final_x = None
        self.final_y = None
        self.has_piece = None
        self.is_dragging = False
        self.images = Image("standard")
        self.image_dict = self.images.image_dictionary(math.floor(SQUARE * 1.2))
        self.image = None

    def set_init_pos(self, x, y, curr_player="white"):
        # Set initial drag position based on player
        self.x = x
        self.y = y
        self.initial_x, self.initial_y = self.calculate_indices(x, y, curr_player)

    def update_final_pos(self, x, y, curr_player="white"):
        # Update final drag position based on player
        self.x = x
        self.y = y
        self.final_x, self.final_y = self.calculate_indices(x, y, curr_player)

    def calculate_indices(self, row, col, curr_player):
        if curr_player == "white":
            return (row // SQUARE, col // SQUARE)
        else:
            return (ROWS - (row // SQUARE) - 1, COLS - (col // SQUARE) - 1)

    def clear_drag(self):
        # Clear drag attributes
        self.image = None

    def get_final_pos(self):
        # Get the final drag position
        return (self.final_x, self.final_y)

    def get_init_pos(self):
        # Get the initial drag position
        return (self.initial_x, self.initial_y)

    def show_drag_piece(self, screen):
        # Show the dragged piece on the screen
        if self.image is not None:
            image_center = (self.x - DRAG_PIECE, self.y - DRAG_PIECE)
            screen.blit(self.image, image_center)
