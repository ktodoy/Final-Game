import pygame
import time
from dababy import DaBaby
from road import Road

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()
#logo = pygame.image.load("images/kart.png")
#logo.set_colorkey((255,255,255))
dababy = DaBaby()
road = Road()
screen.fill((33,191,143))
screen.blit(road.image, (0,screen_rect.height / 2 - 64))
screen.blit(dababy.image, (0,screen_rect.height / 2))
#screen.blit(logo, (440,360))
bop = pygame.mixer.music.load('sounds/bop.mp3')


pygame.mixer.music.play()

pygame.display.flip()
time.sleep(2)

