import pygame

class DaBaby:

    def __init__(self, dbkart):
        self.image = pygame.image.load('images/dababy.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()
        self.rect.center = dbkart.screen_rect.center
        self.health = 3

        self.y = float(self.rect.y)
        self.rect.x = 100
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.rect.y -= 1
            if self.rect.y <= self.screen_rect.height / 2 - 180:
                self.moving_up = False
        if self.moving_down:
            self.rect.y += 1
            if self.rect.y >= self.screen_rect.height / 2 + 134:
                self.moving_down = False

    def blit_car(self):
        self.screen.blit(self.image, self.rect)


