import pygame
import os

class Image:
    def __init__(self,piece_type:str) -> None:
        self.piece_type = piece_type
        self.pieces = ["pawn","bishop","knight","rook","king","queen"]
        self.colors = ["black","white"]
        self.image_dict = {}
        self.image_list()

    def image_list(self):
        for color in self.colors:
            for piece in self.pieces:
                image_path = os.path.join(f"/gameAssets/images/{color}-{piece}-{self.piece_type}.png")
                self.image_dict[f"{color}-{piece}"] = pygame.image.load(image_path)
        
        return self.image_dict
