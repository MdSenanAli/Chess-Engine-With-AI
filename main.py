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

    def game_loop(self):
        screen = self.screen
        game = self.game
        board = self.game.board.game_board
        drag = self.drag

        while True:
            self.display(game, screen, drag)

            # Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down(screen, game, board, drag)

                elif event.type == pygame.MOUSEMOTION:
                    if drag.is_dragging:
                        x, y = pygame.mouse.get_pos()
                        drag.update_final_pos(x, y)
                        self.display(game, screen, drag)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if drag.is_dragging:
                        x, y = pygame.mouse.get_pos()
                        drag.update_final_pos(x, y)
                        y_f, x_f = drag.get_final_pos()
                        y_i, x_i = drag.get_init_pos()
                        board[x_i][y_i].dragged = False

                        if (x_i, y_i) != (x_f, y_f):
                            board[x_f][y_f] = board[x_i][y_i]
                            board[x_i][y_i] = None

                    drag.clear_drag()

                elif event.type == pygame.QUIT:
                    self.handle_quit()

            pygame.display.update()

    # display function
    def display(self, game, screen, drag):
        game.show_board(screen)
        game.show_pieces(screen)
        drag.show_drag_piece(screen)

    def handle_quit(self):
        pygame.quit()
        sys.exit()

    def handle_mouse_button_down(self, screen, game, board, drag):
        x, y = pygame.mouse.get_pos()
        drag.set_init_pos(x, y)
        x = x // SQUARE
        y = y // SQUARE
        if board[y][x] is not None:  # It has a piece
            board[y][x].dragged = True
            piece = board[y][x]
            drag.has_piece = piece
            drag.image = drag.image_dict[piece.name]
            drag.is_dragging = True
            self.display(game, screen, drag)


if __name__ == "__main__":
    main = Main()
    main.game_loop()
