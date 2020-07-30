import random
import pygame


class Powerup:
    def __init__(self, type, img=None, color=(255, 255, 255)):

        # generate a random number 0-5 to pick a string for the obstacle to spawn
        num = random.randint(0, 5)

        if num == 5:
            self._rect = pygame.Rect((600, 27, 30, 30))
        if num == 4:
            self._rect = pygame.Rect((600, 87, 30, 30))
        if num == 3:
            self._rect = pygame.Rect((600, 147, 30, 30))
        if num == 2:
            self._rect = pygame.Rect((600, 207, 30, 30))
        if num == 1:
            self._rect = pygame.Rect((600, 267, 30, 30))
        if num == 0:
            self._rect = pygame.Rect((600, 327, 30, 30))

        self._type = type
        self._color = color
        self._img = img

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        self._img = img