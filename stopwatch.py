import pygame

class Stopwatch:

    def __init__(self, dbkart):
        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.bg = pygame.surface.Surface((160, 40)).convert()
        self.bg.fill((33, 191, 143))
        self.font = pygame.font.SysFont("Carre-JWja.ttf", 60)

    def display_clock(self, dbkart):
        if self.milliseconds > 1000:
            self.seconds += 1
            self.milliseconds -= 1000
            self.screen.blit(self.bg, (64,64))

        if self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60
        self.milliseconds += self.clock.tick_busy_loop(360) # have to keep this number high in order for game to function at a proper frame rate
        self.timer = self.font.render("{}:{}:{}".format(self.minutes, self.seconds, self.milliseconds), True, (0, 0, 0))
        self.screen.blit(self.timer, (dbkart.screen_rect.width / 20, dbkart.screen_rect.width / 15))
