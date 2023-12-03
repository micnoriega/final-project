import pygame
import random
from PIL import Image

class SpaceBackground(pygame.sprite.Sprite):
    def __init__ (self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class DuckSprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.move_x = 0
        self.move_y = 0

    '''def movement(self, x, y):
        self.move_x += x
        self.move_y +- y

    def update(self):
        self.rect.x = self.rect.x + self.move_x
        self.rect.y = self.rect.y + self.move_y'''


        


def main():
    pygame.init()
    pygame.display.set_caption("Exploring Space :D")
    resolution = (1280, 720)
    screen = pygame.display.set_mode(resolution)
    
    x = 0
    y = 0
    width = 50
    height = 50
    move = 2
    Background = SpaceBackground('exploring_space.png', [0,0])
    duck = DuckSprite('duck sprite.png', [0,0])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit()

        
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
        screen.fill([0, 0, 0])
        screen.blit(Background.image, Background.rect)
        #Cat Generation
        pygame.font.init()
        font = pygame.font.SysFont("Courier New", 30)
        screen.blit(font.render("/\\_/\\", True, (255,255,255)), (10, 10))
        screen.blit(font.render(">^w^<", True, (255,255,255)), (10, 50))
        screen.blit(font.render("(___)", True, (255,255,255)), (10, 90))
        screen.blit(duck.image, duck.rect)
        pygame.draw.rect(screen, (255,0,0), (x, y, width, height))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()