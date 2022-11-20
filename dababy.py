import pygame

class DaBaby:

    def __init__(self):
        self.image = pygame.image.load('images/dababy.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
