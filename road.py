import pygame

class Road:

    def __init__(self):
        self.image = pygame.surface.Surface((64, 384))  # makes the road one group/image
        self.image.blit(pygame.image.load('images/top_road.png'), (0, 0))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 64))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 128))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 192))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 256))
        self.image.blit(pygame.image.load('images/bottom_road.png'), (0, 320))
        self.rect = self.image.get_rect()