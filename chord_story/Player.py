import pygame


class Player:
    def __init__(self):
        self._rect = pygame.Rect(200, 200, 10, 26)
        # self._rect = pygame.Rect(100, 100, 5, 13)
        self._lives = 3
        # TODO: replace player image with new sprite
        self._img = pygame.image.load("assets/images/player.png").convert()
        self._score = 0
        self._total_score = 0
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
    def total_score(self):
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        self._total_score = total_score

    @property
    def powerup(self):
        return self._powerup

    @powerup.setter
    def powerup(self, powerup):
        self._powerup = powerup