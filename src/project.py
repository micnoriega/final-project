import pygame
import random
from PIL import Image

class SpaceBackground(pygame.sprite.Sprite):
    def __init__ (self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class DuckSprite(object):
    def __init__(self):
        self.image = pygame.image.load("duck sprite.png")
        self.x = 0
        self.y = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        move = 2
        if keys[pygame.K_w]:
            self.y -= move
        if keys[pygame.K_a]:
            self.x -= move
        if keys[pygame.K_s]:
            self.y += move
        if keys[pygame.K_d]:
            self.x += move

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))        


class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(random.randrange(255), random.randrange(255), random.randrange(255))
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

        


def main():
    pygame.init()
    # display and background
    pygame.display.set_caption("Exploring Space :D")
    resolution = (1280, 720)
    screen = pygame.display.set_mode(resolution)
    Background = SpaceBackground('exploring_space.png', [0,0])
    duck = DuckSprite()
    particles = []
    for num in range(20):
        rand_pos = (random.randrange(resolution[0]+1),
                    random.randrange(resolution[1]+1))
        particles.append(Particle(pos=rand_pos))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit()

        
        #movement mechanics
        duck.movement()

        # render & display
        screen.fill([0, 0, 0])
        screen.blit(Background.image, Background.rect)
        # cat Generation
        pygame.font.init()
        font = pygame.font.SysFont("Courier New", 20)
        screen.blit(font.render("/\\_/\\", True, (random.randrange(255), random.randrange(255), random.randrange(255))), (10, 10))
        screen.blit(font.render(">^w^<", True, (random.randrange(255), random.randrange(255), random.randrange(255))), (10, 37))
        screen.blit(font.render("(___)", True, (random.randrange(255), random.randrange(255), random.randrange(255))), (10, 60))
        # duck generation + movement
        duck.draw(screen)
        for particle in particles:
            particle.draw(screen)
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()