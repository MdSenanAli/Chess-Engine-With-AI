# Import Pygame
import pygame

# Import all the constants to this file
from constant import *


class Main:
    def __init__(self) -> None:
        # Always initialize the pygame 
        pygame.init()
        pass


main = Main().game_loop()

if "__name__" == "__main__":
    main()