import pygame
from constants import *
from player import Player
def main():

    # initialize all pygame modules
    pygame.init()

    # Create screen to render game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    clock = pygame.time.Clock()
    dt = 0

    # X and Y values passed in
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Game loop
    while True:
        
        # Check if user has exited and end game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Background of game set to black
        screen.fill("black")
        # Draws player to screen
        player.draw(screen)

        # update the screen
        pygame.display.flip()
        
        # Calculates the detla time of the previously generated frame - limit 60
        dt = clock.tick(60) / 1000

        
    


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
