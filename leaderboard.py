import pygame
import sys
from stopwatch import Stopwatch
from healthbar import HealthBar

class Leaderboard():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.stopwatch = Stopwatch(self)
        self.font1 = pygame.font.SysFont('chalkduster.ttf', 150)
        self.font2 = pygame.font.SysFont('chalkduster.ttf', 35)
        self.score_text = self.font1.render('Your Score:', True, (0,0,0))
        self.play_again = self.font2.render('Play Again', True, (255, 255, 255))
        self.button = pygame.Rect(self.screen_rect.width / 2 - 100, self.screen_rect.height / 2 + 180, 200, 100)
        self.healthbar = HealthBar(self)
        self.healthbar.health == 0
        self.click = False

    def run_leaderboard(self):
        while True:
            self.check_events()
            self.display_leaderboard()

    def display_leaderboard(self):
        self.screen.fill((33, 191, 143))
        self.screen.blit(self.score_text, (self.screen_rect.width / 2 - 300 , self.screen_rect.height / 2 - 300))
        from game import DaBabyKart # to avoid circular import
        self.dbkart = DaBabyKart()
        print(self.dbkart.final_time)
        #self.final_time = f'{self.dbkart.final_time[0]} : {self.dbkart.final_time[1]} : {self.dbkart.final_time[2]}'
        #self.time = self.font1.render(f'{self.final_time}', True, (0,0,0))
        #self.screen.blit(self.time, (self.screen_rect.width / 2 - 300 , self.screen_rect.height / 2 - 100))
        pygame.draw.rect(self.screen, (0, 0, 0), self.button)
        self.screen.blit(self.play_again, (self.screen_rect.width / 2 - 60, self.screen_rect.height / 2 + 220))
        if self.button.collidepoint(pygame.mouse.get_pos()):  # Josh saved me
            pygame.draw.rect(self.screen, (255, 255, 255), self.button)
            if self.click:
                from game import DaBabyKart #to avoid circular import
                self.dbkart = DaBabyKart()
                self.dbkart.run_game()

        pygame.display.flip()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True