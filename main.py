import pygame
from constants import *
from player import Player

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    clock = pygame.time.Clock()
    dt = 0

    while running:

        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()






if __name__ == "__main__":
    main()