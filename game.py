import itertools
import pygame
from board import Board
from constant import *
from image import Image
from drag import Drag


class Game:
    def __init__(self) -> None:
        # Initialize the game's attributes
        self.board = Board()  # Initialize the game board
        self.rotated = False  # Flag to indicate if the board is rotated
        self.current_player = "white"  # Track the current player's turn
        self.drag = Drag()  # Initialize the drag handler

    # Display the chessboard pattern on the screen
    def show_board(self, screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            square_tile = self.calculate_square_rect(
                row, col
            )  # Calculate square position
            color = self.determine_square_color(row, col)  # Determine square color
            self.draw_square(screen, square_tile, color)  # Draw the square

    # Calculate the rectangle for a square on the chessboard
    def calculate_square_rect(self, row, col):
        return pygame.Rect(col * SQUARE, row * SQUARE, SQUARE, SQUARE)

    # Determine the color of a square based on its position
    def determine_square_color(self, row, col):
        return (255, 255, 255) if (row + col) % 2 == 0 else (180, 180, 180)

    # Draw the square on the screen with the specified color
    def draw_square(self, screen, rect, color):
        pygame.draw.rect(screen, color, rect)

    # Display the game pieces on the screen
    def show_pieces(self, screen):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            self.draw_piece(screen, row, col)

    # Draw a game piece on the screen
    def draw_piece(self, screen, row, col):
        piece = self.board.game_board[row][col]
        if piece is not None and not piece.dragged:
            image = piece.image
            image_center = self.calculate_image_center(col, row)
            screen.blit(image, image_center)

    # Calculate the position to draw an image based on the rotation flag
    def calculate_image_center(self, col, row):
        return (
            ((COLS - col - 1) * SQUARE, (ROWS - row - 1) * SQUARE)
            if self.rotated
            else (col * SQUARE, row * SQUARE)
        )

    # Switch the current player's turn and toggle the board rotation
    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"
        self.rotated = not self.rotated
