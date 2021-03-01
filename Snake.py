import pygame, random, math
from const import *


class Snake:

    def __init__(self, start_length, thickness, window):
        self.enVie = True
        self.orientation = 90
        self.dimensions = tuple(int(n / thickness) for n in window)
        self.thickness = thickness
        self.demi = int(thickness/2)
        if start_length <= self.dimensions[0]:
            self.length = start_length
        else:
            self.length = 1
        self.body = [[1 + n, 1] for n in reversed(range(self.length))]
        self.tongue = [[self.body[0][0] + thickness, self.body[0][1] + int(self.thickness/2)],
                       [self.body[0][0] + (2*thickness), self.body[0][1] + int(self.thickness/2)]]
        self.pomme = [self.randpomme(0), self.randpomme(1)]

    def draw(self, surface):
        for bout in self.body:
            pygame.draw.rect(surface, WHITE, (bout[0]*self.thickness, bout[1]*self.thickness, self.thickness, self.thickness))
        pygame.draw.line(surface, RED, tuple(self.tongue[0]), tuple(self.tongue[1]))
        pygame.draw.circle(surface, GREEN, tuple(n*self.thickness + self.demi for n in self.pomme), self.demi)

    def go(self):
        # Déplacement
        for i in reversed(range(1, self.length)):
            self.body[i] = self.body[i - 1].copy()

        if self.orientation == 0:
            self.body[0][1] -= 1
            self.tongue[0] = [(self.body[0][0]*self.thickness) + self.demi, self.body[0][1]*self.thickness]
            self.tongue[1] = [self.tongue[0][0], self.tongue[0][1] - self.thickness]
        elif self.orientation == 90:
            self.body[0][0] += 1
            self.tongue[0] = [(self.body[0][0]*self.thickness) + self.thickness, (self.body[0][1]*self.thickness) + self.demi]
            self.tongue[1] = [self.tongue[0][0] + self.thickness, self.tongue[0][1]]
        elif self.orientation == 180:
            self.body[0][1] += 1
            self.tongue[0] = [(self.body[0][0]*self.thickness) + self.demi, (self.body[0][1]*self.thickness) + self.thickness]
            self.tongue[1] = [self.tongue[0][0], self.tongue[0][1] + self.thickness]
        elif self.orientation == 270:
            self.body[0][0] -= 1
            self.tongue[0] = [self.body[0][0]*self.thickness, (self.body[0][1]*self.thickness) + self.demi]
            self.tongue[1] = [self.tongue[0][0] - self.thickness, self.tongue[0][1]]

        # Vérification des impacts
        if (self.body[0] in self.body[1:]) or (self.body[0][0] not in range(0, self.dimensions[0])) \
                or (self.body[0][1] not in range(0, self.dimensions[1])):
            self.enVie = False

        # Contact avec la pomme
        if self.body[0] == self.pomme:
            self.length += 1
            self.body.append([])
            self.pomme = [self.randpomme(0), self.randpomme(1)]
            self.go()

    def move(self, key):
        if key == pygame.K_LEFT:
            self.orientation -= 90
        elif key == pygame.K_RIGHT:
            self.orientation += 90
        self.orientation %= 360

    def randpomme(self, n):
        return random.randrange(self.dimensions[n])

    def __str__(self):
        DIR = {0: 'nord', 90: 'est', 180: 'sud', 270: 'ouest'}
        return f"< Serpent long de {self.length} et épais de {self.thickness}," \
               f" en position ({self.body[0][0]}, {self.body[0][1]}) et orienté {DIR[self.orientation]} >"
