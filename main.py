import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot 

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        screen.fill((0, 0, 0), rect=None, special_flags=0)   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        Player.containers[0].update(dt)
        for thing in drawable:
            thing.draw(screen)

        for a in asteroids:
            if a.collision(player):
                print("Game Over!")
                return
            for s in shots:
                if a.collision(s):
                    s.kill()
                    a.split()
    

        dt = clock.tick(60)/1000
        #end of loop
        pygame.display.flip()


if __name__ == "__main__":
    main()
