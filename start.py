import pygame
import sys
from game import DaBabyKart
from road import Road

class Start():


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/kart.png')
        self.image_rect = self.image.get_rect()
        self.button_1 = pygame.Rect(self.screen_rect.width / 2 - 100, self.screen_rect.height / 2 - 70, 200, 100)
        self.button_2 = pygame.Rect(self.screen_rect.width / 2 - 100, self.screen_rect.height / 2 + 70, 200, 100)
        self.dbkart = DaBabyKart()
        self.road = Road(self)
        self.click = False

    def run_start(self):
        while True:
            pygame.mixer.music.load('sounds/bop.mp3')
            pygame.mixer.music.play(-1) # plays infinitely
            self.check_events()
            self.display_start()


    def display_start(self):
            self.screen.fill((33, 191, 143))
            for x in range(0, self.screen_rect.width, 64):
                self.screen.blit(self.road.image, (x, self.screen_rect.height / 2 - 180))
            self.screen.blit(self.image, (self.screen_rect.width / 2 - 512 , self.screen_rect.height / 2 - 270 ))
            pygame.draw.rect(self.screen, (0, 0, 0), self.button_1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.button_2)
            if self.button_1.collidepoint(pygame.mouse.get_pos()): #Josh saved me
                pygame.draw.rect(self.screen, (255, 255, 255), self.button_1)
                if self.click:
                    self.dbkart.run_game()
            if self.button_2.collidepoint(pygame.mouse.get_pos()): #Josh saved me
                pygame.draw.rect(self.screen, (255, 255, 255), self.button_2)
                if self.click:
                    self.dbkart.run_game()

            pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

st = Start()
st.run_start()

