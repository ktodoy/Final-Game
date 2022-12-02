import pygame
import random


class Car1():

    def __init__(self, dbkart):

        self.image = pygame.image.load('images/police_car.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()

        self.moving_left = True

        self.rect.x = 1280
        self.rect.y = float(random.randint(186, 490))

    def move_car1(self):
        if self.moving_left == True:
            self.rect.x -= 1

        if self.rect.x <= -80:
            self.rect.x = 1300
            self.rect.y = float(random.randint(186, 490))

    def blit_car1(self):
        self.move_car1()
        self.screen.blit(self.image, self.rect)