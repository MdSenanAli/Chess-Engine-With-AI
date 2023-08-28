import itertools
import pygame
from board import Board
from constant import *
from image import Image

class Game:
    def __init__(self) -> None:
        self.board = Board(PLAY_WHITE)

    
    def show_board(self,screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            square_tile = (row*SQUARE,col*SQUARE,SQUARE,SQUARE)
            color = (255,255,255) if (row+col)%2==0 else (180,180,180) # update this color scheme later
            pygame.draw.rect(screen,color,square_tile)
        
    def show_pieces(self, screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            if self.board.game_board[row][col] is not None:
                image = self.board.game_board[row][col].image
                image_center = (col * SQUARE, row * SQUARE)  # Swap col and row
                
                screen.blit(image, image_center)


