import pygame
import sys
from dababy import DaBaby
from road import Road
from smoothie import Smoothie
from stopwatch import Stopwatch

class DaBabyKart():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.bop = pygame.mixer.Sound('sounds/bop.mp3')
        self.road = Road()
        self.car = DaBaby(self)
        self.smoothie = Smoothie(self)
        self.stopwatch = Stopwatch(self)

    def run_game(self):
        while True:
            self.check_events()
            self.car.update()
            self.car.blit_car()
            self.update_screen()
            self.play_music()

    def play_music(self):
        pygame.mixer.Sound.play(self.bop)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.car.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.car.moving_down = True
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.car.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.car.moving_down = False

    def update_screen(self):
        self.screen.fill((33, 191, 143))
        self.stopwatch.display_clock()
        for x in range(0, self.screen_rect.width, 64):
            self.screen.blit(self.road.image, (x, self.screen_rect.height / 2 - 180))
        self.car.blit_car()
        self.smoothie.blit_smoothie()
        pygame.display.flip()

db = DaBabyKart()
db.run_game()

#logo = pygame.image.load("images/bkart.png")
#logo.set_colorkey((255,255,255))
