import itertools
import pygame
from board import Board
from constant import *
from image import Image

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.rotated = False
        self.current_player = "white"
    
    # This function is responsible for displaying the chessboard on the screen,
    # drawing alternating squares with different colors to create a checkerboard pattern.
    def show_board(self, screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            # Calculate the rectangle for the current square
            square_tile = (row * SQUARE, col * SQUARE, SQUARE, SQUARE)
            
            # Determine the color of the square based on the row and column indices
            color = (255, 255, 255) if (row + col) % 2 == 0 else (180, 180, 180)
            
            # Draw the square on the screen using the determined color
            pygame.draw.rect(screen, color, square_tile)

        
    def show_pieces(self, screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            if self.board.game_board[row][col] is not None:
                image = self.board.game_board[row][col].image
                if not self.rotated:
                    image_center = (col * SQUARE, row * SQUARE)
                else:
                    image_center = ((COLS - col - 1) * SQUARE, (ROWS - row - 1) * SQUARE)
                    
                screen.blit(image, image_center)

    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"
        self.rotated = not self.rotated

