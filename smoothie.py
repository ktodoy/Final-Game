import pygame
import random

class Smoothie:

    def __init__(self, dbkart):
        self.image = pygame.image.load('images/smoothie.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()


        def
            self.rect.x = random.randint(1280, )
            self.rect.y = random.randint(186,490)

            self.x = float(self.rect.x)
