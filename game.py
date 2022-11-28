import pygame
import time
from dababy import DaBaby
from road import Road

class DaBabyKart():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.bop = pygame.mixer.Sound('sounds/bop.mp3')
        self.road = Road()
        self.car = DaBaby()

    def run_game(self):
        pygame.mixer.Sound.play(self.bop)
        self.screen.fill((33, 191, 143))

        for x in range(0, self.screen_rect.width, 64):
            self.screen.blit(self.road.image, (x, self.screen_rect.height / 2 - 160)) #subtract half the height of both images to place it in exact middle
        self.screen.blit(self.car.image, (128, self.screen_rect.height / 2 - 32))

        pygame.display.flip()
        time.sleep(5)

db = DaBabyKart()
db.run_game()



#screen.fill((33,191,143))
#screen.blit(road.image, (0,screen_rect.height / 2 - 64))
#screen.blit(road.image, (64,screen_rect.height / 2 - 64))
#screen.blit(road.image, (128,screen_rect.height / 2 - 64))
#screen.blit(dababy.image, (128, screen_rect.height / 2))

#logo = pygame.image.load("images/kart.png")
#logo.set_colorkey((255,255,255))
#screen.blit(logo, (440,360))