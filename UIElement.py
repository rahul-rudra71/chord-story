import pygame
from pygame.sprite import Sprite

class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, pic, pic2, action=None):
        """
        Args:
            center_position - tuple (x, y)
            pic - path of png button default
            pic2 - path of png button highlighted
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = pygame.image.load(pic)

        highlighted_image = pygame.image.load(pic2)

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
