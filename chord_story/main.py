import sys, os, random
import pygame
from pygame.locals import *
from pygame import mixer
from pydub import AudioSegment

import chord_story.decode_notes as dn
from chord_story.Game import Game
from chord_story.Obstacle import Obstacle
from chord_story.Powerup import Powerup
from chord_story.Player import Player

# initialize display
clock = pygame.time.Clock()
pygame.init()
#mixer.init()
pygame.display.set_caption("Chord Story")
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window
# used as the surface for rendering, which is scaled
# TODO: remove scaling
display = pygame.Surface((600, 400))
# display = pygame.Surface((300, 200))

# initialize game and player
game = Game()
player = Player()


# opens the main menu screen
def main_menu():
    click = False
    menu_open = True

    while menu_open:

        display.fill((255, 255, 255))  # clear screen by filling it with white
        chord = pygame.image.load("assets/images/main.png")
        screen.blit(chord, (0, 0))

        mousex, mousey = pygame.mouse.get_pos()

        ######
        play_image = pygame.image.load("assets/images/buttons/play.png")

        playH_image = pygame.image.load("assets/images/buttons/playH.png")

        rects = [
            play_image.get_rect(center=(150, 100)),
            playH_image.get_rect(center=(150, 100)),
        ]

        screen.blit(play_image, rects[0])
        if rects[0].collidepoint((mousex, mousey)):
            screen.blit(playH_image, rects[1])
            if click:
                #play the game if the button is pressed
                select_difficulty()
                run_game()
        ######

        # create the classic mode button
        #classic_button = pygame.Rect(50, 50, 150, 60)

        # render button
        #pygame.draw.rect(screen, (156, 17, 21), classic_button)

        #highlight = (232, 58, 63)

        #if classic_button.collidepoint((mousex, mousey)):
        #    pygame.draw.rect(screen, highlight, classic_button)
        #    if click:
        #        #play the game if the button is pressed
        #        select_difficulty()
        #        run_game()

        #classic_font = pygame.font.Font("freesansbold.ttf", 17)
        #classic_text = classic_font.render(
        #    "CLASSIC MODE", True, (255, 255, 255))
        #screen.blit(classic_text, (59, 72))

        # TODO: add a game instruction page with controls and other info

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

    while select:
        display.fill((224, 132, 132))  # clear screen by filling it with pink

        pinkbackground = pygame.image.load("assets/images/pink.png")

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


# display the countdown timer
def countdown(seconds):
    font = pygame.font.Font("freesansbold.ttf", 80)
    text = font.render(str(seconds), True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)


# open the pause screen
def paused():
    click = False

    #pygame.mixer.music.pause()

    while game.state == "paused":
        mousex, mousey = pygame.mouse.get_pos()

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
                game.state = "resuming"
                unpause()
                return
        if quit_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight, quit_button)
            if click:
                player.lives = 3
                player.score = 0
                player.powerup = None
                game.obstacles.clear()
                game.powerups.clear()
                game.state = "running"
                main_menu()

        button_font = pygame.font.Font("freesansbold.ttf", 17)
        continue_text = button_font.render("CONTINUE", True, (255, 255, 255))
        quit_text = button_font.render("QUIT", True, (255, 255, 255))
        screen.blit(continue_text, (472, 355))
        screen.blit(quit_text, (65, 355))

        click = False

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                game.state = "exit"
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# unpause the game
def unpause():

    # set the inital timer to 3 seconds
    game.counter = 3
    pygame.time.set_timer(game.events["COUNTDOWN"], 1000)

    background_rect = game.background.get_rect()

    while game.state == "resuming":
        display.fill((255, 255, 255))

        # draw the board
        draw_background(background_rect)
        draw_strings()
        draw_game_objects()
        display.blit(player.img, (player.rect.x, player.rect.y))
        # screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
        screen.blit(display, (0, 0))

        # display the lives and score
        update_lives()
        update_score()

        countdown(game.counter)

        if game.counter == 0:
            game.state = "running"
            player.powerup = None
            #pygame.mixer.music.unpause()

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                game.state = "exit"
                pygame.quit()
                sys.exit()

            # decrement the countdown timer
            if event.type == game.events["COUNTDOWN"]:
                game.counter -= 1

        pygame.display.update()
        clock.tick(60)


# open the restart screen
def restarting():
    click = False

    while game.state == "restarting":
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
                # 3s countdown before level starts
                game.state = "resuming"
                unpause()
                player.lives = 3
                player.score = 0
                player.rect = pygame.Rect(218, 200, 30, 36)
                player.powerup = None
                game.state = "running"
                game.obstacles.clear()
                game.powerups.clear()
                return
        if quit_button.collidepoint((mousex, mousey)):
            pygame.draw.rect(screen, highlight2, quit_button)
            if click:
                player.lives = 3
                player.score = 0
                player.powerup = None
                game.state = "running"
                game.obstacles.clear()
                game.powerups.clear()
                main_menu()

        button_font = pygame.font.Font("freesansbold.ttf", 17)
        restart_text = button_font.render("RESTART", True, (255, 255, 255))
        quit_text = button_font.render("QUIT", True, (255, 255, 255))
        screen.blit(restart_text, (480, 355))
        screen.blit(quit_text, (65, 355))

        click = False

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                game.state = "exit"
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


# check player is in contact with a string
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


# move the player and ground player on string
def move(rect, movement, tiles):
    collision_types = {"top": False, "bottom": False,
                       "right": False, "left": False}
    rect.x += movement[0]

    # keep player withing window bounds
    if rect.right > 599:
        rect.right = 599
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
    for obstacle in obstacles:
        # player loses a life; obstacle hit disappears and the player gets 2s of recovery time
        if player_rect.colliderect(obstacle):
            # TODO: change the player to a damage avatar momentarily (if possible, make flashing animation)
            #effect = pygame.mixer.Sound('assets/sounds/damage.wav')
            effect.play()
            player.lives = player.lives - 1
            obstacles.remove(obstacle)
            player.powerup = "phaser"
            pygame.time.set_timer(game.events["RECOVER"], 2000, True)

        # remove the obstacle once off screen
        if obstacle.rect.right < 0:
            obstacles.remove(obstacle)

        # out of lives = game over
        if player.lives == 0:
            #effect = pygame.mixer.Sound('assets/sounds/lose.wav')
            effect.play()
            game.state = "dead"


# check if player has hit a powerup; set the appropriate behaviors
def powerup_collision(player_rect, powerups):
    for powerup in powerups:
        if player_rect.colliderect(powerup):

            # gain an extra life
            if powerup.type == "life":
                #effect = pygame.mixer.Sound('assets/sounds/life.wav')
                effect.play()
                player.lives += 1

            # invulnerable to obstacles for a bit
            if powerup.type == "phaser":
                player.powerup = "phaser"
                #effect = pygame.mixer.Sound('assets/sounds/powerup.wav')
                effect.play()
                player.img = pygame.image.load("assets/images/player1_invincible.png").convert_alpha()
                pygame.time.set_timer(game.events["PHASERTIMER"], 5000, True)

            powerups.remove(powerup)

        # remove once off screen
        if powerup.rect.right < 0:
            powerups.remove(powerup)


# set the color of the obstacle once it crossing the beat bar
def set_obstacle_color(obstacle):
    # color depends on string
    if obstacle.stringNum == 0:
        obstacle.color = (255, 84, 71)
    if obstacle.stringNum == 1:
        obstacle.color = (255, 181, 71)
    if obstacle.stringNum == 2:
        obstacle.color = (255, 246, 117)
    if obstacle.stringNum == 3:
        obstacle.color = (108, 224, 110)
    if obstacle.stringNum == 4:
        obstacle.color = (142, 185, 245)
    if obstacle.stringNum == 5:
        obstacle.color = (191, 107, 219)


# display the game over screen
def game_over():
    #mixer.music.stop()
    font = pygame.font.Font("freesansbold.ttf", 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)


# display the game won screen
def game_won():
    font = pygame.font.Font("freesansbold.ttf", 80)
    text = font.render("YOU WIN", True, (0, 255, 0))
    text_rect = text.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    #mixer.music.stop()


# update the lives displayed on screen
def update_lives():
    lives_display = pygame.Rect(20, 370, 55, 25)

    pygame.draw.rect(screen, (255, 255, 255), lives_display)

    lives_font = pygame.font.Font("freesansbold.ttf", 12)
    player_lives_str = str(player.lives)
    lives_text = lives_font.render(
        "LIVES: " + player_lives_str, True, (0, 0, 0))
    screen.blit(lives_text, (22, 375))


# update the score displayed on screen
def update_score():
    score_display = pygame.Rect(80, 370, 100, 25)

    pygame.draw.rect(screen, (255, 255, 255), score_display)

    score_font = pygame.font.Font("freesansbold.ttf", 12)
    score_str = str(player.score)
    score_text = score_font.render("SCORE: " + score_str, True, (0, 0, 0))
    screen.blit(score_text, (82, 375))


# draw the guitar strings on the screen
def draw_strings():
    tile_rects = []

    # draw strings
    pygame.draw.line(display, (255, 255, 255), (0, 58), (600, 58), 4)  # line 0
    tile_rects.append(pygame.Rect(0, 58, 600, 4))
    pygame.draw.line(display, (255, 255, 255), (0, 118), (600, 118), 4)  # line 1
    tile_rects.append(pygame.Rect(0, 118, 600, 4))
    pygame.draw.line(display, (255, 255, 255), (0, 178), (600, 178), 4)  # line 2
    tile_rects.append(pygame.Rect(0, 178, 600, 4))
    pygame.draw.line(display, (255, 255, 255), (0, 238), (600, 238), 4)  # line 3
    tile_rects.append(pygame.Rect(0, 238, 600, 4))
    pygame.draw.line(display, (255, 255, 255), (0, 298), (600, 298), 4)  # line 4
    tile_rects.append(pygame.Rect(0, 298, 600, 4))
    pygame.draw.line(display, (255, 255, 255), (0, 358), (600, 358), 4)  # line 5
    tile_rects.append(pygame.Rect(0, 358, 600, 4))

    # draw the obstacle bar
    pygame.draw.line(display, (255, 255, 255), (440, 0), (440, 400), 10)
    # pygame.draw.line(display, (255, 255, 255), (220, 0), (220, 200), 5)

    return tile_rects


# display and scroll the background image
def draw_background(background_rect):

    display.blit(game.background, background_rect)  # left image
    display.blit(
        game.background, background_rect.move(background_rect.width, 0)
    )  # right image
    if game.state == "running":
        background_rect.move_ip(-2, 0)
    if background_rect.right == 0:
        background_rect.x = 0

    return background_rect


# draw obstacles and powerups
def draw_game_objects():
    for obstacle in game.obstacles:
        if game.state == "running":
            # faster obstacle moving speed for higher difficulty
            if game.difficulty == 0.5:  # easy mode
                obstacle.rect.x -= 2
            elif game.difficulty == 0.35:  # medium mode
                obstacle.rect.x -= 4
            elif game.difficulty == 0.25:  # hard mode
                obstacle.rect.x -= 8

            # change color of obstacle after crossing bar
            if obstacle.rect.right < 440 and not obstacle.color_set:
                set_obstacle_color(obstacle)
                obstacle.color_set = True # only set the color once

        pygame.draw.rect(display, obstacle.color, obstacle.rect)

    for powerup in game.powerups:
        if game.state == "running":
            powerup.rect.x -= 4
        display.blit(powerup.img, (powerup.rect.x, powerup.rect.y))


# start playing the music
def start_music():
    # set the delay to start the music so the beats line up
    if game.difficulty == 0.5:  # easy mode
        pygame.time.set_timer(game.events["STARTMUSIC"], 1250, True)
    if game.difficulty == 0.35:  # medium mode
        pygame.time.set_timer(game.events["STARTMUSIC"], 625, True)
    if game.difficulty == 0.25:  # hard mode
        pygame.time.set_timer(game.events["STARTMUSIC"], 312, True)


# main game function with loop
def run_game():
    game.state = "running"

    # initialize movement
    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    # clear the board
    game.obstacles.clear()
    game.powerups.clear()

    # process the audio file
    decode = dn.decode(game.difficulty)

    # if mp3 selected, convert to a temporary wav for pygame mixer compatibility
    if decode[1].endswith(".mp3"):
        sound = AudioSegment.from_mp3(decode[1])
        sound.export(decode[1][:-4] + ".wav", format="wav")

    # load the notes and music
    notes = decode[0]
    #mixer.music.load(decode[1][:-4] + ".wav")
    noteKeys = list(notes.keys())

    # deleted the temporary wav file
    if decode[1].endswith(".mp3"):
        os.remove(decode[1][:-4] + ".wav")

    # get the first note/obstacle
    noteTime = noteKeys[0]
    stringNo = notes[noteTime]

    # start the timers for game events and spawning
    pygame.time.set_timer(game.events["NEWOBSTACLE"], int(noteTime * 1000), True)
    pygame.time.set_timer(game.events["SCOREUP"], 1000)  # update the score every second
    pygame.time.set_timer(game.events["SPAWNLIFE"], 6000)  # spawn a extra life ~3 times per song

    phaser_time = random.randint(30, 90) # spawn a phasing ability every 30 - 90 seconds
    pygame.time.set_timer(game.events["SPAWNPHASER"], phaser_time * 1000)

    # TODO: add bonus point obstacles

    keyIndex = 0

    start_music()

    player.img.set_colorkey((255, 255, 255))

    background_rect = game.background.get_rect()

    while game.state == "running":
        display.fill((255, 255, 255))  # clear screen by filling it with white

        # draw the scrolling background
        background_rect = draw_background(background_rect)

        # draw the guitar strings to screen
        tile_rects = draw_strings()

        # move obstacles and other objects across screen
        draw_game_objects()

        player_movement = [0, 0]

        # move player
        if game.state == "running":
            # TODO: change player facing direction depending on moving direction
            if moving_right == True:
                player_movement[0] += 4
            if moving_left == True:
                player_movement[0] -= 4

            # TODO: add sound effects for jumping (maybe?)
            player_movement[1] += vertical_momentum
            vertical_momentum += 0.4
            if vertical_momentum > 6:
                vertical_momentum = 6

        # check for collisions and grounding
        player.rect, collisions = move(player.rect, player_movement, tile_rects)

        # death if collision with obstacle
        # player passes through and ignores obstacles if possessing phaser ability
        if player.powerup != "phaser":
            obstacle_collision(player.rect, game.obstacles)

        powerup_collision(player.rect, game.powerups)

        for event in pygame.event.get():  # event loop

            # quit on x clicked
            if event.type == QUIT:
                game.state == "exit"
                pygame.quit()
                sys.exit()

            if game.state == "running":
                # move player
                if event.type == KEYDOWN:
                    if event.key == pygame.K_p:
                        game.state = "paused"
                        paused()
                        pygame.time.set_timer(game.events["NEWOBSTACLE"], int(noteDiffTime * 1000), True)
                    if event.key == K_RIGHT:
                        moving_right = True
                    if event.key == K_LEFT:
                        moving_left = True
                    if event.key == K_UP:
                        if air_timer < 12:
                            vertical_momentum = -6
                    if event.key == K_DOWN:
                        if air_timer < 12:
                            vertical_momentum = 6
                        player.rect.y += 50
                        if player.rect.y > 331:
                            player.rect.y = 331

                # stop moving on release
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        moving_right = False
                    if event.key == K_LEFT:
                        moving_left = False

                # spawn a new obstacle
                if event.type == game.events["NEWOBSTACLE"]:
                    if (stringNo != ''):
                        obstacle = Obstacle(stringNo)
                        game.obstacles.append(obstacle)

                    keyIndex = keyIndex + 1

                    # if end of song, win
                    if keyIndex > len(noteKeys) - 1:
                        #effect = pygame.mixer.Sound('assets/sounds/win.wav')
                        effect.play()
                        game.state = "won"
                        break

                    noteTime = noteKeys[keyIndex]
                    noteDiffTime = noteKeys[keyIndex] - noteKeys[keyIndex - 1]
                    stringNo = notes[noteTime]

                    # set the timer to spawn the next obstacle
                    pygame.time.set_timer(game.events["NEWOBSTACLE"], int(noteDiffTime * 1000), True)

                # increase the score every second; higher difficulty = greater increment
                if event.type == game.events["SCOREUP"]:
                    player.score += (1 - game.difficulty) * 20
                    player.total_score += (1 - game.difficulty) * 20

                # spawn a life every minute
                if event.type == game.events["SPAWNLIFE"]:
                    life = Powerup("life", pygame.image.load("assets/images/life.png").convert())
                    life.img.set_colorkey((255, 255, 255))
                    game.powerups.append(life)

                # spawn a phaser powerup
                if event.type == game.events["SPAWNPHASER"]:
                    phaser = Powerup("phaser", pygame.image.load("assets/images/invincible.png").convert())
                    phaser.img.set_colorkey((255, 255, 255))
                    game.powerups.append(phaser)

                    # set time to spawn the next phaser powerup
                    phaser_time = random.randint(30, 90)
                    pygame.time.set_timer(game.events["SPAWNPHASER"], phaser_time * 1000)

                # phaser powerup lasts for 5s
                if event.type == game.events["PHASERTIMER"] and player.powerup == "phaser":
                    player.powerup = None
                    #effect = pygame.mixer.Sound('assets/sounds/powerdown.wav')
                    effect.play()
                    player.img = pygame.image.load("assets/images/player1.png").convert()
                    player.img.set_colorkey((255, 255, 255))

                # start the music with a delay so the obstacles line up with the bar
                #if event.type == game.events["STARTMUSIC"]:
                    #mixer.music.play()

                # players gets 2s of recover time after losing a life or unpausing the game
                if event.type == game.events["RECOVER"]:
                    player.powerup = None

        display.blit(player.img, (player.rect.x, player.rect.y))

        screen.blit(display, (0, 0))
        # screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

        # display the lives and score
        update_lives()
        update_score()

        # dead - game over screen; restart level or quit
        if game.state == "dead":
            game_over()
            game.state = "restarting"
            restarting()

            noteTime = noteKeys[0]
            stringNo = notes[noteTime]
            keyIndex = 0

            pygame.time.set_timer(game.events["NEWOBSTACLE"], int(noteTime * 1000), True)

            start_music()

        # win - show game win screen; start new level or quit
        if game.state == "won":
            game_won()
            game.state = "restarting"
            restarting()
            game.obstacles.clear()
            game.powerups.clear()

            noteTime = noteKeys[0]
            stringNo = notes[noteTime]
            keyIndex = 0

            pygame.time.set_timer(game.events["NEWOBSTACLE"], int(noteTime * 1000), True)

            start_music()

        pygame.display.update()
        clock.tick(120)
