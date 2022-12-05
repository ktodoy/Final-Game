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

    def make_lines(self):
        self.line_1 = pygame.image.load('images/line.png')
        self.line_1.rect = self.line_1.get_rect()
        self.line_2 = pygame.image.load('images/line.png')
        self.line_2.rect = self.line_2.get_rect()
        self.line_3 = pygame.image.load('images/line.png')
        self.line_3.rect = self.line_3.get_rect()
        self.line_4 = pygame.image.load('images/line.png')
        self.line_4.rect = self.line_4.get_rect()
        self.line_5 = pygame.image.load('images/line.png')
        self.line_5.rect = self.line_5.get_rect()
        self.line_6 = pygame.image.load('images/line.png')
        self.line_6.rect = self.line_6.get_rect()
        self.line_7 = pygame.image.load('images/line.png')
        self.line_7.rect = self.line_7.get_rect()
        self.line_8 = pygame.image.load('images/line.png')
        self.line_8.rect = self.line_8.get_rect()
        self.line_9 = pygame.image.load('images/line.png')
        self.line_9.rect = self.line_9.get_rect()
        self.line_10 = pygame.image.load('images/line.png')
        self.line_10.rect = self.line_10.get_rect()
        self.line_11 = pygame.image.load('images/line.png')
        self.line_11.rect = self.line_11.get_rect()
        self.line_12 = pygame.image.load('images/line.png')
        self.line_12.rect = self.line_12.get_rect()
        self.line_13 = pygame.image.load('images/line.png')
        self.line_13.rect = self.line_13.get_rect()
        self.line_14 = pygame.image.load('images/line.png')
        self.line_14.rect = self.line_14.get_rect()
        self.line_15 = pygame.image.load('images/line.png')
        self.line_15.rect = self.line_15.get_rect()
        self.line_16 = pygame.image.load('images/line.png')
        self.line_16.rect = self.line_16.get_rect()


    def move_line(self):
        if self.moving_left == True:
            self.line_1.rect.x -= 1
            self.line_2.rect.x -= 1
            self.line_3.rect.x -= 1
            self.line_4.rect.x -= 1
            self.line_5.rect.x -= 1
            self.line_6.rect.x -= 1
            self.line_7.rect.x -= 1
            self.line_8.rect.x -= 1
            self.line_9.rect.x -= 1
            self.line_10.rect.x -= 1
            self.line_11.rect.x -= 1
            self.line_12.rect.x -= 1
            self.line_13.rect.x -= 1
            self.line_14.rect.x -= 1
            self.line_15.rect.x -= 1
            self.line_16.rect.x -= 1

        if self.rect.x <= -80:
            self.rect.x = self.screen_rect.width + 20
            self.rect.y = self.screen.height / 2 + 8


    def blit_line(self):
        self.screen.blit(self.line, self.rect)