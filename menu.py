import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
from UIElement import UIElement
import decode_notes

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

class Player:
    """ Stores information about a player """

    def __init__(self, levels=[]):
        self.levels = levels


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    player = Player()
    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.CREATEGAME:
            game_state = create_level(screen, player)

        if game_state == GameState.CREATE_LEVEL:
            keys = decode_notes.decode()
            print(keys)
            game_state = create_level(screen, player)

        if game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen):
    start_btn = UIElement(
        center_position=(400, 400),
        pic="playButton.png",
        pic2="backButton.png",
        action=GameState.CREATEGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        pic="backButton.png",
        pic2="playButton.png",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn, quit_btn)

    return game_loop(screen, buttons)


def create_level(screen, player):
    return_btn = UIElement(
        center_position=(140, 570),
        pic="backButton.png",
        pic2="playButton.png",
        action=GameState.TITLE,
    )

    nextlevel_btn = UIElement(
        center_position=(400, 400),
        pic="playButton.png",
        pic2="backButton.png",
        action=GameState.CREATE_LEVEL,
    )

    buttons = RenderUpdates(return_btn, nextlevel_btn)

    return game_loop(screen, buttons)


def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    CREATEGAME = 1
    CREATE_LEVEL = 2


if __name__ == "__main__":
    main()
