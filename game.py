import pygame
import sys
from dababy import DaBaby
from road import Road
from potion import Potion
from stopwatch import Stopwatch
from car1 import Car1
from car2 import Car2
from car3 import Car3
from car4 import Car4

class DaBabyKart():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.bop = pygame.mixer.Sound('sounds/bop.mp3')
        self.ha = pygame.mixer.Sound('sounds/ha.mp3')
        self.road = Road()
        self.dababy = DaBaby(self)
        self.potion = Potion(self)
        self.stopwatch = Stopwatch(self)
        self.car1 = Car1(self)
        self.car2 = Car2(self)
        self.car3 = Car3(self)
        self.car4 = Car4(self)
        self.car1_collision = pygame.sprite.collide_rect(self.dababy, self.car1)
        self.car2_collision = pygame.sprite.collide_rect(self.dababy, self.car2)
        self.car3_collision = pygame.sprite.collide_rect(self.dababy, self.car3)
        self.car4_collision = pygame.sprite.collide_rect(self.dababy, self.car4)
        self.potion_collision = pygame.sprite.collide_rect(self.dababy, self.potion)

        self.blit_car1 = True

    def run_game(self):
        while True:
            self.check_events()
            self.dababy.update()
            self.dababy.blit_car()
            self.check_collision()
            self.update_screen()
            self.play_music()

    def play_music(self):
        pygame.mixer.Sound.play(self.bop)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.dababy.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.dababy.moving_down = True
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.dababy.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.dababy.moving_down = False

    def draw_cars(self):
        if self.blit_car1 == True:
            self.car1.move_car1(self)
            self.car1.blit_car1()

        if self.blit_car1 == True:
            self.car2.move_car2(self)
            self.car2.blit_car2()

        if self.stopwatch.seconds >= 10:
            self.car3.move_car3(self)
            self.car3.blit_car3()
        elif self.stopwatch.minutes >= 1:
            self.car3.move_car3(self)
            self.car3.blit_car3()

        if self.stopwatch.seconds >= 30:
            self.car4.blit_car4()
        elif self.stopwatch.minutes >= 1:
            self.car4.blit_car4()

    def draw_potion(self):
        if self.stopwatch.seconds >= 30:
            self.potion.blit_potion()
            if self.stopwatch.seconds % 30 == 0:
                self.potion.rect.x = self.screen_rect.width + 20
        elif self.stopwatch.minutes >= 1:
            self.potion.blit_potion()
            if self.stopwatch.seconds % 30 == 0:
                self.potion.rect.x = self.screen_rect.width + 20
    def update_screen(self):
        self.screen.fill((33, 191, 143))
        for x in range(0, self.screen_rect.width, 64):
            self.screen.blit(self.road.image, (x, self.screen_rect.height / 2 - 180))
        self.dababy.blit_car()
        self.stopwatch.display_clock(self)
        self.screen.blit(self.dababy.image, (self.screen_rect.width / 7 * 6, self.screen_rect.width/15))
        self.screen.blit(self.dababy.image, (self.screen_rect.width / 7 * 6 - 64, self.screen_rect.width/15))
        self.screen.blit(self.dababy.image, (self.screen_rect.width / 7 * 6 - 128, self.screen_rect.width/15))

        self.draw_cars()
        self.draw_potion()
        self.dababy.blit_car()

        pygame.display.flip()

    def check_collision(self):
        if self.car1_collision:
            self.blit_car1 = False
        elif self.car2_collision:
            self.dababy.health -= 1
        elif self.car3_collision:
            self.dababy.health -= 1
        elif self.car4_collision:
            self.dababy.health -= 1

db = DaBabyKart()
db.run_game()

#logo = pygame.image.load("images/bkart.png")
#logo.set_colorkey((255,255,255))
