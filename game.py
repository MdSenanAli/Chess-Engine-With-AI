import itertools
import pygame
from board import Board
from constant import *
from image import Image

class Game:
    def __init__(self) -> None:
        self.board = Board
        self.image_set = Image("standard")

    
    def show_board(self,screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            square_tile = (row*SQUARE,col*SQUARE,SQUARE,SQUARE)
            color = (255,255,255) if (row+col)%2==0 else (180,180,180) # update this color scheme later
            pygame.draw.rect(screen,color,square_tile)
                