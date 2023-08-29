from image import Image
from constant import *
import math


class Drag:
    def __init__(self) -> None:
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
        self.x = x
        self.y = y
        if curr_player == "white":
            self.initial_x = x // SQUARE
            self.initial_y = y // SQUARE
        else:
            self.initial_x = ROWS - (x // SQUARE) - 1
            self.initial_y = COLS - (y // SQUARE) - 1

    def update_final_pos(self, x, y, curr_player="white"):
        self.x = x
        self.y = y
        if curr_player == "white":
            self.final_x = x // SQUARE
            self.final_y = y // SQUARE
        else:
            self.final_x = ROWS - (x // SQUARE) - 1
            self.final_y = COLS - (y // SQUARE) - 1

    def clear_drag(self):
        self.initial_x = None
        self.initial_y = None
        self.final_x = None
        self.final_y = None
        self.has_piece = None
        self.is_dragging = False
        self.image = None

    def get_final_pos(self):
        return (self.final_x, self.final_y)

    def get_init_pos(self):
        return (self.initial_x, self.initial_y)

    def show_drag_piece(self, screen):
        if self.image is not None:
            image_center = (self.x - 50, self.y - 50)
            screen.blit(self.image, image_center)
