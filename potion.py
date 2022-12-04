import pygame
import random
from stopwatch import Stopwatch
from pygame.sprite import Sprite

class Potion(Sprite):

    def __init__(self, dbkart):
        super().__init__()
        self.image = pygame.image.load('images/potion.png')
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()
        self.stopwatch = Stopwatch(self)

        self.rect.x = dbkart.screen_rect.width + 20
        self.rect.y = float(random.randint(self.screen_rect.height / 2 - 180, self.screen_rect.height / 2 + 134))

        self.moving_left = True

    def move_potion(self):
        if self.moving_left == True:
            self.rect.x -= 1

    def blit_potion(self):
        self.move_potion()
        self.screen.blit(self.image, self.rect)




