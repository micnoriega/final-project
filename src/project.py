import pygame
import random
from PIL import Image, ImageFilter

def generate_sprite(filename):
    with (Image.open("duck sprite.png") as sprite):
        x = 100
        y = 100


def main():
    pygame.init()
    pygame.display.set_caption("Game :D")
    resolution = (960, 540)
    screen = pygame.display.set_mode(resolution)
    sprite = generate_sprite(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Render & Display
        lightBlue = pygame.Color(210, 226, 252)
        screen.fill(lightBlue)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()