import pygame

class HealthBar():

    def __init__(self, dbkart):
        pygame.init()

        self.screen = dbkart.screen
        self.screen_rect = dbkart.screen.get_rect()
        self.health = 500
        self.max_health = 500
        self.bar_length = 300
        self.ratio = self.max_health / self.bar_length

    def do_damage(self):
        if self.health > 0:
            self.health -= 2
        if self.health <= 0:
            self.health = 0

    def add_health(self):
        if self.health <= self.max_health:
            self.health = self.max_health

    def draw_healthbar(self):
        pygame.draw.rect(self.screen, (0,255,0), (self.screen_rect.width - 500, self.screen_rect.width / 15, self.health / self.ratio, 25))
        pygame.draw.rect(self.screen, (255,255,255), (self.screen_rect.width - 500, self.screen_rect.width / 15, self.bar_length, 25), 4)
