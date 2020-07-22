import random, pygame


class Powerup:
    def __init__(self, type, color = (0, 0, 0)):

        # generate a random number 0-5 to pick a string for the obstacle to spawn
        num = random.randint(0, 5)

        if num == 5:
            self._rect = pygame.Rect((300, 15, 15, 15))
        if num == 4:
            self._rect = pygame.Rect((300, 45, 15, 15))
        if num == 3:
            self._rect = pygame.Rect((300, 75, 15, 15))
        if num == 2:
            self._rect = pygame.Rect((300, 105, 15, 15))
        if num == 1:
            self._rect = pygame.Rect((300, 135, 15, 15))
        if num == 0:
            self._rect = pygame.Rect((300, 165, 15, 15))

        self._type = type
        self._color = color

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