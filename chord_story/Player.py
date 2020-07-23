import pygame


class Player:
    def __init__(self):
        self._rect = pygame.Rect(100, 100, 5, 13)
        self._lives = 3
        self._img = pygame.image.load("assets/player.png").convert()
        self._score = 0
        self._powerup = None

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        self._lives = lives

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        self._img = img

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def powerup(self):
        return self._powerup

    @powerup.setter
    def powerup(self, powerup):
        self._powerup = powerup
