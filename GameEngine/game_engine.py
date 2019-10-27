import sys
import pygame
from enum import Enum


class CarMovement(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class GameEngine:
    def __init__(self, screen_size):
        self.game_event_key = list()
        self.initiated = False
        if pygame.init():
            self.screen = pygame.display.set_mode(screen_size)

            # init background
            self.background = (0, 0, 0)
            self.screen.fill(self.background)
            pygame.display.update()

            # init car
            car_image = pygame.image.load('car.png')
            transform_car_image = pygame.transform.rotate(pygame.transform.scale(car_image, (100, 50)), -90)
            self.car = Car(self.screen, transform_car_image, 10, 1)

            self.running = True
            self.initiated = True

    def getEvents(self):
        events = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.car.move(CarMovement.UP)
                if event.key == pygame.K_DOWN:
                    self.car.move(CarMovement.DOWN)
                if event.key == pygame.K_LEFT:
                    self.car.move(CarMovement.LEFT)
                if event.key == pygame.K_RIGHT:
                    self.car.move(CarMovement.RIGHT)

    def update(self):
        self.getEvents()

        # First place the background
        self.screen.fill(self.background)

        # Update car
        self.car.update()

        # Update screen
        pygame.display.update()
        pygame.time.delay(10)

    def kill(self):
        if self.initiated:
            sys.exit()


class Car:
    def __init__(self, screen, image, height, speed):
        self.screen = screen
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def update(self):
        self.screen.blit(self.image, self.pos)

    def move(self, move_type):
        if move_type == CarMovement.UP:
            self.pos = self.pos.move(0, -self.speed)
        elif move_type == CarMovement.DOWN:
            self.pos = self.pos.move(0, self.speed)
        elif move_type == CarMovement.LEFT:
            self.pos = self.pos.move(-self.speed, 0)
        elif move_type == CarMovement.RIGHT:
            self.pos = self.pos.move(self.speed, 0)
        self.checkBounds()

    def checkBounds(self):
        if self.pos.right > 600:
            self.pos.left = 0
