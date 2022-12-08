import pygame
import math
from pygame.sprite import Sprite

class Car5(Sprite):

    def __init__(self, dbkart):
        super().__init__()
        self.image = pygame.image.load('images/police_car.png')
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()

        self.moving_left = True
        self.t = pygame.time.get_ticks()/3 % self.screen_rect.width


    def blit_car5(self):
        if self.moving_left:
            self.rect.x = self.t
            self.rect.y = math.sin(self.t / 50) * 100 + 200
            self.screen.blit(self.image, self.rect)
