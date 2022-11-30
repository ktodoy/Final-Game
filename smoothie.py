import pygame
import random
from stopwatch import Stopwatch

class Smoothie:

    def __init__(self, dbkart):
        self.image = pygame.image.load('images/smoothie.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()
        self.x = float(self.rect.x)
        self.stopwatch = Stopwatch(self)

        self.rect.x = 1280
        self.rect.y = float(random.randint(186, 490))

        self.moving_left = True

    def move_smoothie(self):
        if self.moving_left == True:
            self.rect.x -= 4

        if self.rect.x == -80:
            self.rect.x = 1280
            self.rect.y = float(random.randint(186, 490))

    def blit_smoothie(self):
        self.move_smoothie()
        self.screen.blit(self.image, self.rect)


