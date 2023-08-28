import itertools
import pygame
from constant import *
from piece import *
from image import Image

class Board:
    def __init__(self,player) -> None:
        self.game_board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.piece_arrangement = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        self.image_set = Image("standard")
        self.images = self.image_set.image_list()
        self.human_player = player
        self.initialise_board(player)
        if self.human_player == PLAY_BLACK:
            self.rotate_board()

    def initialise_board(self,playing_side):
        my_pawn_location = playing_side[0][0]
        enemy_pawn_location = playing_side[1][0]

        print(my_pawn_location,enemy_pawn_location)

        my_color,enemy_color = ("white","black") if playing_side == PLAY_WHITE else ("black","white")
        # enemy_color = "black" if playing_side == PLAY_WHITE else "white"

        for col in range(COLS):

            self.game_board[my_pawn_location][col] = Pawn(my_color,self.images[f"{my_color}-pawn"])
            self.game_board[enemy_pawn_location][col] = Pawn(enemy_color,self.images[f"{enemy_color}-pawn"])
        
        my_piece_location = playing_side[0][1]
        enemy_piece_location = playing_side[1][1]
        
        for col in range(COLS):
            self.game_board[my_piece_location][col] = self.piece_arrangement[col](my_color,self.images[f"{my_color}-pawn"])
            self.game_board[enemy_piece_location][col] = self.piece_arrangement[col](enemy_color,self.images[f"{enemy_color}-pawn"])

    def rotate_board(self):
        for row in range(ROWS):
            self.game_board[row] = list(reversed(self.game_board[row]))
        self.game_board = list(reversed(self.game_board))