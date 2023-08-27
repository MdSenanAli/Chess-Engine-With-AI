# Import Pygame
import pygame
import sys

# Import all the constants to this file
from constant import *

# from game import Game


class Main:
    def __init__(self) -> None:
        # Always initialize the pygame
        pygame.init()
        pygame.display.set_caption("Chess Engine - Mohammad Senan Ali")

        # Initialising the screen for the pygame display main window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def game_loop(self):
        screen = self.screen

        while True:
            # Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event == pygame.MOUSEBUTTONDOWN:
                    print("clicked")
                    
            list_item = ['a','b','c','d']
            for i in list_item:
                print(list_item[i])

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.game_loop()
