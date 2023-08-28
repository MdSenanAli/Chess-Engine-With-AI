import pygame
import os
from constant import *

class Image:
    def __init__(self,piece_type:str) -> None:
        self.piece_type = piece_type
        self.pieces = ["pawn","bishop","knight","rook","king","queen"]
        self.colors = ["black","white"]
        self.image_dict = {}
        # self.image_list()

    def image_list(self):
        for color in self.colors:
            for piece in self.pieces:
                image_path = os.path.join(f"gameAssets\images\{color}-{piece}-{self.piece_type}.png")
                # self.image_dict[f"{color}-{piece}"] = image_path
                self.image_dict[f"{color}-{piece}"] = pygame.transform.scale(pygame.image.load(image_path),(SQUARE,SQUARE))
        
        return self.image_dict
