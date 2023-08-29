# Import Pygame
import pygame
import sys

# Import all the constants to this file
from constant import *
from move import Move
from game import Game
from drag import Drag

# from game import Game


class Main:
    def __init__(self) -> None:
        # Always initialize the pygame
        pygame.init()
        pygame.display.set_caption("Chess Engine - Mohammad Senan Ali")

        # Initialising the screen for the pygame display main window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game()
        self.drag = self.game.drag

    def get_mouse_position(self):
        mouse_loc_x, mouse_loc_y = pygame.mouse.get_pos()
        tile_x, tile_y = mouse_loc_x // SQUARE, mouse_loc_y // SQUARE
        return (
            (tile_x, tile_y)
            if self.game.current_player == "white"
            else (ROWS - tile_x - 1, COLS - tile_y - 1)
        )

    def game_loop(self):
        screen = self.screen
        game = self.game
        board = self.game.board.game_board
        drag = self.drag

        while True:
            game.show_board(screen)
            game.show_pieces(screen)

            # Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Will add more code
                    x, y = self.get_mouse_position()
                    drag.set_init_pos(x, y)

                    if board[y][x] is not None:  # It has a piece
                        piece = board[y][x]
                        drag.has_piece = piece
                        drag.is_dragging = True

                elif event.type == pygame.MOUSEMOTION:
                    if drag.is_dragging:
                        x, y = self.get_mouse_position()
                        drag.update_final_pos(x, y)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if drag.is_dragging:
                        x, y = self.get_mouse_position()
                        drag.update_final_pos(x, y)
                        y_f, x_f = drag.get_final_pos()
                        y_i, x_i = drag.get_init_pos()
                        if (x_i, y_f) != (x_f, y_f):
                            board[x_f][y_f] = board[x_i][y_i]
                            board[x_i][y_i] = None

                    drag.clear_drag()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.game_loop()
