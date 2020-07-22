import pygame


class Player:
    def __init__(self):
        self._player_rect = pygame.Rect(100, 100, 5, 13)
        self._player_lives = 3
        self._player_img = pygame.image.load("assets/player.png").convert()
        self._score = 0

    @property
    def player_rect(self):
        return self._player_rect

    @player_rect.setter
    def player_rect(self, player_rect):
        self._player_rect = player_rect

    @property
    def player_lives(self):
        return self._player_lives

    @player_lives.setter
    def player_lives(self, player_lives):
        self._player_lives = player_lives

    @property
    def player_img(self):
        return self._player_img

    @player_img.setter
    def player_img(self, player_img):
        self._player_img = player_img

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
