import pygame
from chord_story.PlayerSprite import PlayerSprite


class Player:
    def __init__(self):
        self._sprite = PlayerSprite()
        self._sprite_group = pygame.sprite.Group(self._sprite)
        self._lives = 3
        self._score = 0
        self._total_score = 0
        self._powerup = None

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, sprite):
        self._sprite = sprite

    @property
    def sprite_group(self):
        return self._sprite_group

    @sprite_group.setter
    def sprite_group(self, sprite_group):
        self._sprite_group = sprite_group

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        self._lives = lives

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
