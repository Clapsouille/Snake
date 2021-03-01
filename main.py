# -*-coding:Latin-1 -*

import sys
from pygame.locals import *
from Snake import *

pygame.init()
pygame.display.set_caption("Sssnake")

# Constantes
WINDOW_SIZE = (500, 500)
FPS = 20
FONT = pygame.font.SysFont('Arial', 50)

# Caractéristiques du serpent
THICKNESS = 10
START_LENGTH = 12

# Définition de l'affichage initial
CLOCK = pygame.time.Clock()
CLOCK.tick(FPS)
SURFACE = pygame.display.set_mode(WINDOW_SIZE)
SURFACE.fill(BLACK)

# Instanciation du serpent
snake = Snake(START_LENGTH, THICKNESS, WINDOW_SIZE)
snake.draw(SURFACE)

# GAME LOOP
while snake.enVie:
    pygame.display.update()
    snake.go()
    SURFACE.fill(BLACK)
    snake.draw(SURFACE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            snake.move(event.key)
    CLOCK.tick(FPS)

txtPerdu = FONT.render('PERDU', False, (255, 255, 255))

# MENU LOOP
while True:
    pygame.display.update()
    SURFACE.blit(txtPerdu, (int(WINDOW_SIZE[0]/4), int(WINDOW_SIZE[1]/4)))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    CLOCK.tick(FPS)