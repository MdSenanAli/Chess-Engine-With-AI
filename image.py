import pygame
import os
from constant import *

# This class manages the loading and scaling of images for chess pieces.
class Image:
    def __init__(self, piece_type: str) -> None:
        # Initialize the image manager with the given piece type.
        self.piece_type = piece_type
        self.pieces = ["pawn", "bishop", "knight", "rook", "king", "queen"]
        self.colors = ["black", "white"]
        self.image_dict = {}
        # self.image_list()

    # Generates and returns a dictionary containing piece images for both colors.
    def image_dictionary(self):
        for color in self.colors:
            for piece in self.pieces:
                image_path = os.path.join(f"gameAssets\images\{color}-{piece}-{self.piece_type}.png")
                
                # Load and scale the image, then store it in the dictionary.
                self.image_dict[f"{color}-{piece}"] = pygame.transform.scale(
                    pygame.image.load(image_path), (SQUARE, SQUARE)
                )
        
        return self.image_dict
