import pygame
import constants as c
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #organizing objects into groups for better handling inside the game loop
    updatable =  pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    shots = pygame.sprite.Group()
    Shot.containers = (drawable, updatable, shots)

    player_character = player.Player(c.SCREEN_WIDTH/2, c.SCREEN_HEIGHT/2)
    field_of_asteroids = AsteroidField()
# The game loop
    while True:
        for event in pygame.event.get(): #the game can be quit by closing the window, or terminal interrupt
            if event.type == pygame.QUIT:
                return
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player_character):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill((0, 0, 0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        clock.tick(60) #limit the game to 60 fps
        dt = clock.tick(60)/1000





if __name__ == "__main__":
        main()
