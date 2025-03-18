import pygame
from constants import *

def main():

    # initialize all pygame modules
    pygame.init()

    # Create screen to render game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        
        # Check if user has exited and end game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Cover the entire screen
        screen.fill("black")

    


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
