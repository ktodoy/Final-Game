import pygame

class Road:

    def __init__(self):
        self.image = pygame.surface.Surface((64, 192))  # makes the road one group/image
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 64))
        self.image.blit(pygame.image.load('images/top_road.png'), (0, 0))
        self.image.blit(pygame.image.load('images/bottom_road.png'), (0, 128))
        self.rect = self.image.get_rect()