import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        self._background = pygame.image.load("assets/images/background.png")
        self._difficulty = 0.25
        self._state = "running"
        self._obstacles = []
        self._powerups = []
        self._counter = 0
        self._events = {
            "NEWOBSTACLE": USEREVENT + 1,
            "SCOREUP": USEREVENT + 2,
            "SPAWNLIFE": USEREVENT + 3,
            "SPAWNPHASER": USEREVENT + 4,
            "PHASERTIMER": USEREVENT + 5,
            "STARTMUSIC": USEREVENT + 6,
            "RECOVER": USEREVENT + 7,
            "COUNTDOWN": USEREVENT + 8
        }

    @property
    def background(self):
        return self._background

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def obstacles(self):
        return self._obstacles

    @obstacles.setter
    def obstacles(self, obstacles):
        self._obstacles = obstacles

    @property
    def powerups(self):
        return self._powerups

    @powerups.setter
    def powerups(self, powerups):
        self._powerups = powerups

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, counter):
        self._counter = counter

    @property
    def events(self):
        return self._events