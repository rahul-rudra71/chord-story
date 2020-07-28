
import random
import pygame


class Obstacle:
    def __init__(self, stringNo, length):

        num = int(stringNo)

        if num == 5:
            self._rect = pygame.Rect((300, 15, length, 15))
        if num == 4:
            self._rect = pygame.Rect((300, 45, length, 15))
        if num == 3:
            self._rect = pygame.Rect((300, 75, length, 15))
        if num == 2:
            self._rect = pygame.Rect((300, 105, length, 15))
        if num == 1:
            self._rect = pygame.Rect((300, 135, length, 15))
        if num == 0:
            self._rect = pygame.Rect((300, 165, length, 15))

        self._color = (255, 255, 255)

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
