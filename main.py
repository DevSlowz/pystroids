import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

import random

def main():

    # initialize all pygame modules
    pygame.init()

    # Create screen to render game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    clock = pygame.time.Clock()
    dt = 0

    # Game groups 
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers =(updateable)
    Shot.containers = (shots, updateable, drawable)
    # X and Y values passed in for player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # X and Y values passed in for asteroid
    asteroid_field = AsteroidField()



    # Game loop
    while True:
        
        # Check if user has exited and end game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Background of game set to black
        screen.fill("black")
        
        # Draws player to screen
        # Draw all the drawables to the screen
        # player.draw(screen)
        for item in drawable:
            item.draw(screen)

        # Update plaer postion before each frame is generated 
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collison_check(player):
                print("GAME OVER!")
                return 

            for shot in shots:
                if  asteroid.collison_check(shot):
                    shot.kill()
                    asteroid.split()

        # update the screen
        pygame.display.flip()
        
        # Calculates the detla time of the previously generated frame - limit 60
        dt = clock.tick(60) / 1000

        
    


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()