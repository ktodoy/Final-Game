import pygame


class Road:
    def __init__(self, dbkart):
        self.image = pygame.surface.Surface((64, 384))  # makes the road one group/image
        self.image.blit(pygame.image.load('images/top_road.png'), (0, 0))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 64))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 128))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 192))
        self.image.blit(pygame.image.load('images/mid_road.png'), (0, 256))
        self.image.blit(pygame.image.load('images/bottom_road.png'), (0, 320))
        self.rect = self.image.get_rect()
        self.moving_left = True
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()
        self.line = pygame.image.load('images/line.png')
        self.line_rect = self.line.get_rect()

    def move_line(self, dbkart):
        if self.moving_left == True:
            self.line_rect.x -= 8

            if self.line_rect.x <= -80:
                self.line_rect.x = dbkart.screen_rect.width + 20
                self.line_rect.y = dbkart.screen_rect.height / 2 - 8

    def blit_line(self):
        self.screen.blit(self.line, self.line_rect)