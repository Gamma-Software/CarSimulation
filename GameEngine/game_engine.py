import sys

import pygame
from pygame.locals import *


class GameEngine:
    def __init__(self):
        self.initiated = False
        if pygame.init():
            self.screen = pygame.display.set_mode((640, 480))
            self.background = (0, 0, 0)
            self.screen.fill(self.background)
            pygame.display.update()
            self.car = GameObject(
                pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load('car.png'), (100, 50)), -90), 10, 1)
            self.running = True
            self.initiated = True

    def update(self):
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                self.running = False

        self.screen.fill(self.background)
        self.car.move()
        self.screen.blit(self.car.image, self.car.pos)
        pygame.display.update()
        pygame.time.delay(10)

    def kill(self):
        if self.initiated:
            sys.exit()


class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
