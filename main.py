import pygame, os, sys, random
import chord_story.decode_notes as dn
from pygame.locals import *
from pygame import mixer
from chord_story.Obstacle import Obstacle
from chord_story.Player import Player

clock = pygame.time.Clock()

pygame.init()
mixer.init()

pygame.display.set_caption("Chord Story")

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window

display = pygame.Surface(
    (300, 200)
)  # used as the surface for rendering, which is scaled

game = Game()
# background = pygame.image.load("chord_story/background.png")
background_size = game.background.get_size()
background_rect = game.background.get_rect()
w, h = background_size
x = 0
y = 0
x1 = 0
y1 = -h


# difficulty = 0.25

player = Player()

obstacles = []

# global running
# running = True


# opens the main menu screen
def main_menu():
    click = False
    menu_open = True
    while menu_open:

        display.fill((255, 255, 255))  # clear screen by filling it with white

        chord = pygame.image.load("chord_story/mainmenu.png")

        screen.blit(chord, (0, 0))

        mousex, mousey = pygame.mouse.get_pos()

        # create the classic mode button
        classic_button = pygame.Rect(50, 50, 150, 60)

        # render button
        pygame.draw.rect(screen, (156, 17, 21), classic_button)

        highlight = (232, 58, 63)

        if classic_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, classic_button)
            if click:
                # play the game if the button is pressed
                select_difficulty()
                run_game()

        classic_font = pygame.font.Font("freesansbold.ttf", 17)
        classic_text = classic_font.render("CLASSIC MODE", True, (255, 255, 255))
        screen.blit(classic_text, (59, 72))

        click = False

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                menu_open = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# sets the difficulty level of the current game
def select_difficulty():
    click = False
    select = True

    # global difficulty

    while select:
        display.fill((224, 132, 132))  # clear screen by filling it with pink

        pinkbackground = pygame.image.load("chord_story/pink.png")

        screen.blit(pinkbackground, (0, 0))

        font = pygame.font.Font("freesansbold.ttf", 45)
        text = font.render("CHOOSE THE DIFFICULTY", True, (0, 0, 0))
        text2 = font.render("CHOOSE THE DIFFICULTY", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, 45))
        text_rect2 = text.get_rect(center=((screen.get_width() / 2) + 2, 47))
        screen.blit(text, text_rect)
        screen.blit(text2, text_rect2)

        mousex, mousey = pygame.mouse.get_pos()

        easy_button = pygame.Rect(screen.get_width() / 2 - 72.5, 100, 145, 60)
        medium_button = pygame.Rect(screen.get_width() / 2 - 72.5, 200, 145, 60)
        hard_button = pygame.Rect(screen.get_width() / 2 - 72.5, 300, 145, 60)

        # render buttons
        pygame.draw.rect(screen, (255, 255, 255), easy_button)
        pygame.draw.rect(screen, (255, 255, 255), medium_button)
        pygame.draw.rect(screen, (255, 255, 255), hard_button)

        highlight = (212, 221, 255)

        # harder difficult = smaller interval between notes
        if easy_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, easy_button)
            if click:
                game.difficulty = 0.5
                select = False
        if medium_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, medium_button)
            if click:
                game.difficulty = 0.35
                select = False
        if hard_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, hard_button)
            if click:
                game.difficulty = 0.25
                select = False

        # easy text
        font = pygame.font.Font("freesansbold.ttf", 35)
        text = font.render("EASY", True, (0, 0, 0))
        text2 = font.render("EASY", True, (224, 132, 132))
        screen.blit(text, (247, 116))
        screen.blit(text2, (249, 118))

        # medium text
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("MEDIUM", True, (0, 0, 0))
        text2 = font.render("MEDIUM", True, (224, 132, 132))
        screen.blit(text, (237, 216))
        screen.blit(text2, (239, 218))

        # hard text
        font = pygame.font.Font("freesansbold.ttf", 35)
        text = font.render("HARD", True, (0, 0, 0))
        text2 = font.render("HARD", True, (224, 132, 132))
        screen.blit(text, (247, 316))
        screen.blit(text2, (249, 318))

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# close the pause screen
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


# open the pause screen
def paused():
    click = False
    pause_screen = True
    while pause_screen:

        mousex, mousey = pygame.mouse.get_pos()

        pygame.mixer.music.pause()

        # create the buttons used to get back into the game or quit
        continue_button = pygame.Rect(470, 340, 95, 50)
        quit_button = pygame.Rect(40, 340, 95, 50)

        # pause message on the screen
        pause_font = pygame.font.Font("freesansbold.ttf", 80)
        pause_text = pause_font.render("PAUSE", True, (255, 0, 0))
        text_rect = pause_text.get_rect(
            center=(screen.get_width() / 2, screen.get_height() / 2)
        )
        screen.blit(pause_text, text_rect)

        # render buttons
        pygame.draw.rect(screen, (156, 17, 21), continue_button)
        pygame.draw.rect(screen, (156, 17, 21), quit_button)

        highlight = (232, 58, 63)

        # highlight buttons on mouse hover
        if continue_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, continue_button)
            if click:
                unpause()
                return
        if quit_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, quit_button)
            if click:
                pause_screen = False
                main_menu()

        button_font = pygame.font.Font("freesansbold.ttf", 17)
        continue_text = button_font.render("CONTINUE", True, (255, 255, 255))
        quit_text = button_font.render("QUIT", True, (255, 255, 255))
        screen.blit(continue_text, (472, 355))
        screen.blit(quit_text, (65, 355))

        click = False

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                pause_screen = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# open the restart screen
def restarting():
    click = False

    restart_screen = True

    # global running
    while restart_screen:

        mousex, mousey = pygame.mouse.get_pos()

        # create the buttons used to get back into the game or quit
        restart_button = pygame.Rect(470, 340, 95, 50)
        quit_button = pygame.Rect(40, 340, 95, 50)

        # render buttons
        pygame.draw.rect(screen, (52, 224, 69), restart_button)
        pygame.draw.rect(screen, (156, 17, 21), quit_button)

        highlight1 = (110, 255, 124)
        highlight2 = (232, 58, 63)

        # highlight buttons on hover
        if restart_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight1, restart_button)
            if click:
                # global player_lives
                player.player_lives = 3
                restart_screen = False
                break
        if quit_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight2, quit_button)
            if click:
                player.player_lives = 3
                restart_screen = False
                # running = True
                game.state = "running"
                main_menu()

        button_font = pygame.font.Font("freesansbold.ttf", 17)
        restart_text = button_font.render("RESTART", True, (255, 255, 255))
        quit_text = button_font.render("QUIT", True, (255, 255, 255))
        screen.blit(restart_text, (480, 355))
        screen.blit(quit_text, (65, 355))

        click = False

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                restart_screen = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# check if objects are colliding
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


# move the player and ground player on string
def move(rect, movement, tiles):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    rect.x += movement[0]

    # keep player withing window bounds
    if rect.right > 299:
        rect.right = 299
    if rect.x < 0:
        rect.x = 0

    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
    return rect, collision_types


# check if player has hit an obstacle
def obstacle_collision(player_rect, obstacles):
    # global player_lives

    # if collision, decrement lives
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            player.player_lives = player.player_lives - 1
            obstacles.remove(obstacle)
        if obstacle.rect.left < -15:
            obstacles.remove(obstacle)
        if player.player_lives == 0:
            # return False
            game.state = "dead"

    # return True


# display the game over screen
def game_over():
    font = pygame.font.Font("freesansbold.ttf", 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    mixer.music.stop()


# display the game won screen
def game_won():
    font = pygame.font.Font("freesansbold.ttf", 80)
    text = font.render("YOU WIN", True, (0, 255, 0))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    mixer.music.stop()


# update the lives displayed on screen
def update_lives():
    lives_display = pygame.Rect(20, 370, 55, 25)

    pygame.draw.rect(screen, (255, 255, 255), lives_display)

    lives_font = pygame.font.Font("freesansbold.ttf", 12)
    player_lives_str = str(player.player_lives)
    lives_text = lives_font.render("LIVES: " + player_lives_str, True, (0, 0, 0))
    screen.blit(lives_text, (22, 375))


# main game function with loop
def run_game():
    global pause
    play_game = True
    game.state = "running"
    # won = False

    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    # true_scroll = [0, 0]

    # player_img = pygame.image.load("chord_story/player.png").convert()
    # player_img.set_colorkey((255, 255, 255))

    # player_rect = pygame.Rect(100, 100, 5, 13)

    decode = dn.decode(game.difficulty)

    notes = decode[0]
    mixer.music.load(decode[1])
    noteKeys = list(notes.keys())

    noteTime = noteKeys[0]
    stringNo = notes[noteTime]

    NEWOBSTACLE = USEREVENT + 1
    pygame.time.set_timer(NEWOBSTACLE, int(noteTime * 1000))

    keyIndex = 0
    mixer.music.play()

    while play_game:  # game loop
        display.fill((255, 255, 255))  # clear screen by filling it with white

        # scrolling background
        display.blit(game.background, background_rect)  # left image
        display.blit(
            game.background, background_rect.move(background_rect.width, 0)
        )  # right image
        if game.state == "running":
            background_rect.move_ip(-1, 0)
        if background_rect.right == 0:
            background_rect.x = 0

        tile_rects = []

        # draw strings
        pygame.draw.line(display, (255, 255, 255), (0, 29), (400, 29), 2)  # line 0
        tile_rects.append(pygame.Rect(0, 29, 400, 2))
        pygame.draw.line(display, (255, 255, 255), (0, 59), (400, 59), 2)  # line 1
        tile_rects.append(pygame.Rect(0, 59, 400, 2))
        pygame.draw.line(display, (255, 255, 255), (0, 89), (400, 89), 2)  # line 2
        tile_rects.append(pygame.Rect(0, 89, 400, 2))
        pygame.draw.line(display, (255, 255, 255), (0, 119), (400, 119), 2)  # line 3
        tile_rects.append(pygame.Rect(0, 119, 400, 2))
        pygame.draw.line(display, (255, 255, 255), (0, 149), (400, 149), 2)  # line 4
        tile_rects.append(pygame.Rect(0, 149, 400, 2))
        pygame.draw.line(display, (255, 255, 255), (0, 179), (400, 179), 2)  # line 5
        tile_rects.append(pygame.Rect(0, 179, 400, 2))

        # move obstacles across screen
        for obstacle in obstacles:
            if game.state == "running":
                obstacle.rect.x -= 2
            pygame.draw.rect(display, (255, 255, 255), obstacle.rect)

        player_movement = [0, 0]

        # move player
        if game.state == "running":
            if moving_right == True:
                player_movement[0] += 2
            if moving_left == True:
                player_movement[0] -= 2
            player_movement[1] += vertical_momentum
            vertical_momentum += 0.2
            if vertical_momentum > 3:
                vertical_momentum = 3

        # check for collisions and grounding
        player.player_rect, collisions = move(
            player.player_rect, player_movement, tile_rects
        )

        # death if collision with obstacle
        # running = obstacle_collision(player.player_rect, obstacles)
        obstacle_collision(player.player_rect, obstacles)
        # alive = running

        for event in pygame.event.get():  # event loop

            # quit on x clicked
            if event.type == QUIT:
                game.state == "exit"
                play_game = False
                pygame.quit()
                sys.exit()

            # move player
            if event.type == KEYDOWN and game.state == "running":
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        vertical_momentum = -3
                if event.key == K_DOWN:
                    if air_timer < 6:
                        vertical_momentum = 3
                    player.player_rect.y += 12
                    if player.player_rect.y > 166:
                        player.player_rect.y = 166

            # stop moving on release
            if event.type == KEYUP and game.state == "running":
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False

            # spawn a new obstacle
            if event.type == NEWOBSTACLE and game.state == "running":
                obstacle = Obstacle(stringNo)
                obstacles.append(obstacle)

                keyIndex = keyIndex + 1

                if keyIndex > len(noteKeys) - 1:
                    game.state = "won"
                    break

                noteTime = noteKeys[keyIndex]

                noteDiffTime = noteKeys[keyIndex] - noteKeys[keyIndex - 1]
                stringNo = notes[noteTime]

                # set the timer to spawn the next obstacle
                pygame.time.set_timer(NEWOBSTACLE, int(noteDiffTime * 1000))

        display.blit(player.player_img, (player.player_rect.x, player.player_rect.y))

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

        # display the lives
        update_lives()

        # dead - game over screen; restart level or quit
        if game.state == "dead":
            game_over()
            restarting()
            game.state == "running"

            noteTime = noteKeys[0]
            stringNo = notes[noteTime]

            pygame.time.set_timer(NEWOBSTACLE, int(noteTime * 1000))

            keyIndex = 0
            mixer.music.play()

        # win - show game win screen; start new level or quit
        if game.state == "won":
            game_won()
            restarting()

            noteTime = noteKeys[0]
            stringNo = notes[noteTime]

            pygame.time.set_timer(NEWOBSTACLE, int(noteTime * 1000))

            keyIndex = 0
            mixer.music.play()

        pygame.display.update()
        clock.tick(120)
