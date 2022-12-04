import pygame
import random
from pygame.sprite import Sprite

class Car1(Sprite):

    def __init__(self, dbkart):
        super().__init__()
        self.image = pygame.image.load('images/police_car.png')
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()

        self.moving_left = True

        self.rect.x = dbkart.screen_rect.width + 20
        self.rect.y = float(random.randint(186, 490))

    def move_car1(self, dbkart):
        if self.moving_left == True:
            self.rect.x -= 1

        if self.rect.x <= -80:
            self.rect.x = dbkart.screen_rect.width + 20
            self.rect.y = float(random.randint(self.screen_rect.height / 2 - 180, self.screen_rect.height / 2 + 134))

    def blit_car1(self):
        self.screen.blit(self.image, self.rect)