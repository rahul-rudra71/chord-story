import pygame


class Game:
    def __init__(self):
        self._background = pygame.image.load("assets/background.png")
        self._difficulty = 0.25
        self._state = "running"

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
