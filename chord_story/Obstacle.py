import pygame


class Obstacle:
    def __init__(self, stringNo):

        num = int(stringNo)

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

        self._color = (255, 255, 255)
        self._stringNum = num
        self._color_set = False

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def stringNum(self):
        return self._stringNum

    @stringNum.setter
    def stringNum(self, stringNum):
        self._stringNum = stringNum

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def color_set(self):
        return self._color_set

    @color_set.setter
    def color_set(self, color_set):
        self._color_set = color_set
