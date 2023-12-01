import pygame
import random
from PIL import Image

'''def generate_sprite(filename):
    with (Image.open("exploring_space.png") as bg,
          Image.open("duck sprite.png") as sprite):
        x = 100
        y = 100
        bg.paste(sprite, (x, y), mask=sprite.getchannel('A'))
        bg.show()'''
class SpaceBackground(pygame.sprite.Sprite):
    def __init__ (self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Duck(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        


def main():
    pygame.init()
    pygame.display.set_caption("Exploring Space :D")
    resolution = (960, 540)
    screen = pygame.display.set_mode(resolution)
    move = 5
    Background = SpaceBackground('exploring_space.png', [0,0])
    #sprite = generate_sprite(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #movement mechanics
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y -= move
        if keys[pygame.K_a]:
            x -= move
        if keys[pygame.K_s]:
            y += move
        if keys[pygame.K_d]:
            x += move

        # Render & Display
        #lightBlue = pygame.Color(210, 226, 252)
        #screen.fill(lightBlue)
        #pygame.display.flip()
        screen.fill([0, 0, 0])
        screen.blit(Background.image, Background.rect)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()