import pygame

class Stopwatch:

    def __init__(self, dbkart):
        self.screen = dbkart.screen
        self.clock = pygame.time.Clock()
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.bg = pygame.surface.Surface((160, 40)).convert()
        self.bg.fill((33, 191, 143))
        self.font = pygame.font.SysFont("dababy_font.ttf", 25)

    def display_clock(self):
        if self.milliseconds > 1000:
            self.seconds += 1
            self.milliseconds -= 1000
            self.screen.blit(self.bg, (64,64))

        if self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60
        self.milliseconds += self.clock.tick_busy_loop(60)
        self.timer = self.font.render("{}:{}:{}".format(self.minutes, self.seconds, self.milliseconds), True, (0, 0, 0))
        self.screen.blit(self.timer, (64, 64))