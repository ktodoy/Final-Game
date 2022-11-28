import pygame

class DaBaby:

    def __init__(self):
        self.image = pygame.image.load('images/dababy.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += 1
