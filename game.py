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
from healthbar import HealthBar
from leaderboard import Leaderboard


class DaBabyKart():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.lets_go = pygame.mixer.Sound('sounds/lets_go.mp3')
        self.ha = pygame.mixer.Sound('sounds/ha.mp3')
        self.road = Road(self)
        self.dababy = DaBaby(self)
        self.potion = Potion(self)
        self.stopwatch = Stopwatch(self)
        self.car1 = Car1(self)
        self.car2 = Car2(self)
        self.car3 = Car3(self)
        self.car4 = Car4(self)
        self.healthbar = HealthBar(self)
        self.leaderboard = Leaderboard()

        self.final_minute = []
        self.final_second = []
        self.final_millisecond = []
        self.final_time = []

    def run_game(self):
        while True:
            self.check_events()
            self.dababy.update()
            self.dababy.blit_car()
            self.check_collision()
            self.update_screen()
            self.get_final_time()
            self.display_leaderboard()

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

    def draw_car12(self):
        self.car1.move_car1(self)
        self.car1.blit_car1()

        self.car2.move_car2(self)
        self.car2.blit_car2()

    def draw_car3(self):
        if self.stopwatch.seconds >= 10:
            self.car3.move_car3(self)
            self.car3.blit_car3()
        elif self.stopwatch.minutes >= 1:
            self.car3.move_car3(self)
            self.car3.blit_car3()

    def draw_car4(self):
        if self.stopwatch.seconds >= 30:
            self.car4.move_car4(self)
            self.car4.blit_car4()
        elif self.stopwatch.minutes >= 1:
            self.car4.move_car4(self)
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
        self.road.move_line(self)
        self.road.blit_line()
        self.dababy.blit_car()
        self.stopwatch.display_clock(self)
        self.draw_car12()
        self.draw_car3()
        self.draw_car4()
        self.draw_potion()
        self.healthbar.draw_healthbar()
        self.dababy.blit_car()

        pygame.display.flip()

    def check_collision(self):
        if pygame.sprite.collide_rect(self.dababy, self.car1):
            self.healthbar.do_damage()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.ha)
            pygame.mixer.music.unpause()
        elif pygame.sprite.collide_rect(self.dababy, self.car2):
            self.healthbar.do_damage()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.ha)
            pygame.mixer.music.unpause()
        elif pygame.sprite.collide_rect(self.dababy, self.car3):
            self.healthbar.do_damage()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.ha)
            pygame.mixer.music.unpause()
        elif pygame.sprite.collide_rect(self.dababy, self.car4):
            self.healthbar.do_damage()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.ha)
            pygame.mixer.music.unpause()
        elif pygame.sprite.collide_rect(self.dababy, self.potion):
            self.healthbar.add_health()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.lets_go)
            pygame.mixer.music.unpause()

    def get_final_time(self):
        if self.healthbar.health == 0:
            self.final_minute.append(self.stopwatch.minutes)
            self.final_second.append(self.stopwatch.seconds)
            self.final_millisecond.append(self.stopwatch.milliseconds)

    def display_leaderboard(self):
        if self.healthbar.health == 0:
            self.final_time.append(self.final_minute[0])
            self.final_time.append(self.final_second[0])
            self.final_time.append(self.final_millisecond[0])
            print(self.final_time)

            self.leaderboard.run_leaderboard()
