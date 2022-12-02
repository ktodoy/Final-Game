import pygame
import random

class Car4():

    def __init__(self, dbkart):

        self.image = pygame.image.load('images/police_car.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()

        self.moving_left = True

        self.rect.x = 1280
        self.rect.y = float(random.randint(186, 490))

    def move_car4(self):
        if self.moving_left == True:
            self.rect.x -= 4

        if self.rect.x <= -4500: #car is fast, so I want it to travel across the screen less frequently
            self.rect.x = 1300
            self.rect.y = float(random.randint(186, 490))

    def blit_car4(self):
        self.move_car4()
        self.screen.blit(self.image, self.rect)