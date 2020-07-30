import sys, os, random, time
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
mixer.init()
pygame.display.set_caption("Chord Story")
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window
display = pygame.Surface((600, 400)) # surface for rendering
player_display = pygame.Surface((600, 400)) # surface for rendering the player

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

        # creates the play button on the home screen
        play_image = pygame.image.load("assets/images/buttons/play.png")
        playH_image = pygame.image.load("assets/images/buttons/playH.png")

        playRects = [
            play_image.get_rect(center=(415, 180)),
            playH_image.get_rect(center=(415, 180)),
        ]

        screen.blit(play_image, playRects[0])
        if playRects[0].collidepoint((mousex, mousey)):
            screen.blit(playH_image, playRects[1])
            if click:
                #play the game if the button is pressed
                select_difficulty()
                run_game()

        # creates the about button on the home screen
        about_image = pygame.image.load("assets/images/buttons/about.png")
        aboutH_image = pygame.image.load("assets/images/buttons/aboutH.png")

        aboutRects = [
            about_image.get_rect(center=(415, 300)),
            aboutH_image.get_rect(center=(415, 300)),
        ]

        screen.blit(about_image, aboutRects[0])
        if aboutRects[0].collidepoint((mousex, mousey)):
            screen.blit(aboutH_image, aboutRects[1])
            if click:
                display_about()
                print("hello")

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


def display_about():
    click = False

    about_open = True

    while about_open:
        display.fill((0, 0, 0))  # clear screen
        aboutScreen = pygame.image.load("assets/images/abtBackground.png")
        screen.blit(aboutScreen, (0, 0))

        # create the back button
        back_image = pygame.image.load("assets/images/buttons/back.png")
        backH_image = pygame.image.load("assets/images/buttons/backH.png")

        backRects = [
            back_image.get_rect(center=(155, 335)),
            backH_image.get_rect(center=(155, 335)),
        ]

        mousex, mousey = pygame.mouse.get_pos()

        screen.blit(back_image, backRects[0])
        if backRects[0].collidepoint((mousex, mousey)):
            screen.blit(backH_image, backRects[1])
            if click:
                aboutMenuOpen = False
                main_menu()

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
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
        display.fill((0, 0, 0))  # clear screen

        selectDifficultyScreen = pygame.image.load("assets/images/difficultyFrame.png")
        screen.blit(selectDifficultyScreen, (0, 0))


        # creates the easy medium and hard buttons on the select difficulty screen
        easy_image = pygame.image.load("assets/images/buttons/easy.png")
        easyH_image = pygame.image.load("assets/images/buttons/easyH.png")

        med_image = pygame.image.load("assets/images/buttons/med.png")
        medH_image = pygame.image.load("assets/images/buttons/medH.png")

        hard_image = pygame.image.load("assets/images/buttons/hard.png")
        hardH_image = pygame.image.load("assets/images/buttons/hardH.png")

        easyRects = [
            easy_image.get_rect(center=(300, 130)),
            easyH_image.get_rect(center=(300, 130)),
        ]

        medRects = [
            med_image.get_rect(center=(300, 230)),
            medH_image.get_rect(center=(300, 230)),
        ]

        hardRects = [
            hard_image.get_rect(center=(300, 330)),
            hardH_image.get_rect(center=(300, 330)),
        ]

        mousex, mousey = pygame.mouse.get_pos()

        screen.blit(easy_image, easyRects[0])
        if easyRects[0].collidepoint((mousex, mousey)):
            screen.blit(easyH_image, easyRects[1])
            if click:
                game.difficulty = 0.5
                select = False

        screen.blit(med_image, medRects[0])
        if medRects[0].collidepoint((mousex, mousey)):
            screen.blit(medH_image, medRects[1])
            if click:
                game.difficulty = 0.35
                select = False

        screen.blit(hard_image, hardRects[0])
        if hardRects[0].collidepoint((mousex, mousey)):
            screen.blit(hardH_image, hardRects[1])
            if click:
                game.difficulty = 0.25
                select = False


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
    font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 80)
    font1 = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 84)
    text = font.render(str(seconds), True, (255, 255, 255))
    text1 = font.render(str(seconds), True, (0, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text1, text_rect)
    screen.blit(text, text_rect)


# open the pause screen
def paused():
    click = False
    pause_time = time.time()
    pygame.mixer.music.pause()

    while game.state == "paused":
        mousex, mousey = pygame.mouse.get_pos()

        # create the buttons used to get back into the game or quit
        continue_button = pygame.Rect(470, 340, 95, 50)
        quit_button = pygame.Rect(40, 340, 95, 50)

        # pause message on the screen
        pause_font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 80)
        pause_text = pause_font.render("PAUSE", True, (255, 0, 0))
        pause_font1 = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 84)
        pause_text1 = pause_font1.render("PAUSE", True, (255, 255, 255)) # second layer of text for a border
        text_rect = pause_text.get_rect(
            center=(screen.get_width() / 2, screen.get_height() / 2)
        )
        screen.blit(pause_text1, text_rect)
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
                return time.time() - pause_time
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

        button_font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 17)
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
        draw_background()
        draw_strings()
        draw_game_objects()
        player.sprite_group.draw(player_display)
        screen.blit(display, (0, 0))

        # display the lives and score
        update_lives()
        update_score()

        countdown(game.counter)

        if game.counter == 0:
            game.state = "running"
            player.powerup = None
            pygame.mixer.music.unpause()

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
                player.sprite.rect = pygame.Rect(218, 200, 30, 36)
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

        button_font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 17)
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


# updates the sprite to the damaged version
def damaged_sprite():
    images = []

    images.append(pygame.image.load("assets/images/sprites/player_damaged1.png").convert())
    images.append(pygame.image.load("assets/images/sprites/player_damaged2.png").convert())

    player.sprite.images = images
    player.sprite_group = pygame.sprite.Group(player.sprite)


# updates the sprite to the invincible version
def invincible_sprite():
    images = []

    images.append(pygame.image.load("assets/images/sprites/player_invincible1.png").convert())
    images.append(pygame.image.load("assets/images/sprites/player_invincible2.png").convert())

    player.sprite.images = images
    player.sprite_group = pygame.sprite.Group(player.sprite)


# updates the sprite to the normal version
def normal_sprite():
    images = []

    images.append(pygame.image.load("assets/images/sprites/player1.png").convert())
    images.append(pygame.image.load("assets/images/sprites/player2.png").convert())

    player.sprite.images = images
    player.sprite_group = pygame.sprite.Group(player.sprite)


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
    if rect.y < 0:
        rect.y = 0

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
            # TODO: make a version of player sprite with red filter
            damaged_sprite()
            player.sprite_group.update()
            effect = pygame.mixer.Sound('assets/sounds/damage.wav')
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
            effect = pygame.mixer.Sound('assets/sounds/lose.wav')
            effect.play()
            game.state = "dead"


# check if player has hit a powerup; set the appropriate behaviors
def powerup_collision(player_rect, powerups):
    for powerup in powerups:
        if player_rect.colliderect(powerup):

            # gain an extra life
            if powerup.type == "life":
                # number of lives is capped at 3
                if player.lives < 3:
                    effect = pygame.mixer.Sound('assets/sounds/life.wav')
                    effect.play()
                    player.lives += 1

            # invulnerable to obstacles for a bit
            if powerup.type == "phaser":
                player.powerup = "phaser"
                effect = pygame.mixer.Sound('assets/sounds/powerup.wav')
                effect.play()
                # TODO make invincible version of player sprite
                invincible_sprite()
                player.sprite_group.update()
                pygame.time.set_timer(game.events["PHASERTIMER"], 5000, True) # 5s of invulnerability

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
    mixer.music.stop()
    font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    font1 = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 84)
    text1 = font1.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text1, text_rect)
    screen.blit(text, text_rect)


# display the game won screen
def game_won():
    font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 80)
    text = font.render("YOU WIN", True, (0, 255, 0))
    font1 = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 84)
    text1 = font1.render("YOU WIN", True, (0, 255, 0))
    text_rect = text.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text1, text_rect)
    screen.blit(text, text_rect)
    mixer.music.stop()


# update the lives displayed on screen
def update_lives():
    # lives_display = pygame.Rect(20, 370, 55, 25)

    # pygame.draw.rect(screen, (255, 255, 255), lives_display)

    lives_font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 12)
    lives_font1 = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 14)
    player_lives_str = str(player.lives)
    lives_text = lives_font.render("LIVES: " + player_lives_str, True, (255, 255, 255))
    lives_text1 = lives_font1.render("LIVES: " + player_lives_str, True, (0, 255, 255))
    screen.blit(lives_text1, (21, 374))
    screen.blit(lives_text, (22, 375))


# update the score displayed on screen
def update_score():
    # score_display = pygame.Rect(80, 370, 100, 25)

    # pygame.draw.rect(screen, (255, 255, 255), score_display)

    score_font = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 12)
    score_font1 = pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", 14)
    score_str = str(player.score)
    score_text = score_font.render("SCORE: " + score_str, True, (255, 255, 255))
    score_text1 = score_font.render("SCORE: " + score_str, True, (0, 255, 255))
    screen.blit(score_text1, (81, 374))
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

    return tile_rects


# display and scroll the background image
def draw_background():

    display.blit(game.background, game.background_rect)  # left image
    display.blit(
        game.background, game.background_rect.move(game.background_rect.width, 0)
    )  # right image
    if game.state == "running":
        game.background_rect.move_ip(-2, 0)
    if game.background_rect.right == 0:
        game.background_rect.x = 0


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
            if obstacle.rect.left < 440 and not obstacle.color_set:
                set_obstacle_color(obstacle)
                obstacle.color_set = True # only set the color once

        pygame.draw.rect(display, obstacle.color, obstacle.rect)

    for powerup in game.powerups:
        if game.state == "running":
            powerup.rect.x -= 4
        display.blit(powerup.img, (powerup.rect.x, powerup.rect.y))


# main game function with loop
def run_game():
    copyDecode = []
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
    decode, filename = dn.decode(game.difficulty)
    copyDecode = decode.copy()
    # if mp3 selected, convert to a temporary wav for pygame mixer compatibility
    if filename.endswith(".mp3"):
        sound = AudioSegment.from_mp3(filename)
        sound.export(filename[:-4] + ".wav", format="wav")

    #get speed of rects
    if game.difficulty == 0.5:  # easy mode
        speed = 2
    elif game.difficulty == 0.35:  # medium mode
        speed = 4
    elif game.difficulty == 0.25:  # hard mode
        speed = 8

    # load the notes and music
    mixer.music.load(filename[:-4] + ".wav")
    # deleted the temporary wav file
    if filename.endswith(".mp3"):
        os.remove(filename[:-4] + ".wav")


    # start the timers for game events and spawning
    pygame.time.set_timer(game.events["SCOREUP"], 1000)  # update the score every second
    pygame.time.set_timer(game.events["SPAWNLIFE"], 60000)  # spawn a extra life every minute

    phaser_time = random.randint(30, 90) # spawn a phasing ability every 30 - 90 seconds
    pygame.time.set_timer(game.events["SPAWNPHASER"], phaser_time * 1000)

    # update the sprite for animation
    pygame.timer.set_timer(game.events["UPDATESPRITE"], 500)

    game.background_rect = game.background.get_rect()

    startGameTime = time.time()
    endGameTime = decode[len(decode) - 1][2]
    mixer.music.play()
    while game.state == "running":
        display.fill((255, 255, 255))  # clear screen by filling it with white

        # draw the scrolling background
        draw_background()

        # draw the guitar strings to screen
        tile_rects = draw_strings()

        # move obstacles and other objects across screen
        draw_game_objects()

        #get and display notes
        timeCheck = round((float(time.time()) - float(startGameTime)), 2)
        #the math is an offset so the bar is on beat
        #offset is: seconds = units * frame/units * secs/frame
        #here it's seconds = 160 * 1/speed * 1/120
        if decode:
          if timeCheck > decode[0][0] - (1.3333333 * (1/speed)):
                stringNo = decode[0][1]
                noteLength = decode[0][2] - (timeCheck + (1.3333333 * (1/speed)))
                if(noteLength <= 0.125):
                  noteLength = 0.125
                if(noteLength >= 3):
                  noteLength = 12 * game.difficulty
                if(stringNo != ''):
                    obstacle = Obstacle(stringNo, round(120 * speed * noteLength))
                    game.obstacles.append(obstacle)
                decode.pop(0)

        player_movement = [0, 0]
        # move player
        if game.state == "running":
            if moving_right == True:
                player_movement[0] += 4
            if moving_left == True:
                player_movement[0] -= 4

            player_movement[1] += vertical_momentum
            vertical_momentum += 0.4
            if vertical_momentum > 6:
                vertical_momentum = 6

        # check for collisions and grounding
        player.sprite.rect, collisions = move(player.sprite.rect, player_movement, tile_rects)

        # death if collision with obstacle
        # player passes through and ignores obstacles if possessing phaser ability
        if player.powerup != "phaser":
            obstacle_collision(player.sprite.rect, game.obstacles)

        powerup_collision(player.sprite.rect, game.powerups)

        #delay 1 second if game won
        if round((float(time.time()) - float(startGameTime)), 2) >= float(endGameTime + 1):
          effect = pygame.mixer.Sound('assets/sounds/win.wav')
          effect.play()
          game.state = "won"

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
                        pauseElapse = paused()
                        startGameTime += pauseElapse
                    if event.key == K_RIGHT:
                        # TODO: change player facing direction depending on moving direction (flip sprite surface?)
                        moving_right = True
                    if event.key == K_LEFT:
                        # TODO: change player facing direction depending on moving direction (flip sprite surface?)
                        moving_left = True
                    if event.key == K_UP:
                        if air_timer < 12:
                            vertical_momentum = -6
                    if event.key == K_DOWN:
                        if air_timer < 12:
                            vertical_momentum = 6
                        player.sprite.rect.y += 50
                        if player.sprite.rect.y > 331:
                            player.sprite.rect.y = 331

                # stop moving on release
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        moving_right = False
                    if event.key == K_LEFT:
                        moving_left = False

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
                    effect = pygame.mixer.Sound('assets/sounds/powerdown.wav')
                    effect.play()
                    normal_sprite()
                    player.sprite_group.update()

                # players gets 2s of recover time after losing a life or unpausing the game
                if event.type == game.events["RECOVER"]:
                    normal_sprite()
                    player.sprite_group.update()
                    player.powerup = None

                # update the sprite image
                if event.type == game.events["UPDATESPRITE"]:
                    # increment the index
                    player.sprite.index += 1
                    player.sprite_group.update()

        player.sprite_group.draw(player_display)

        screen.blit(display, (0, 0))

        # display the lives and score
        update_lives()
        update_score()

        # dead - game over screen; restart level or quit
        if game.state == "dead":
            game_over()
            game.state = "restarting"
            restarting()
            decode = copyDecode.copy()
            startGameTime = time.time()
            mixer.music.play()

        # win - show game win screen; start new level or quit
        if game.state == "won":
            game_won()
            game.state = "restarting"
            restarting()
            game.obstacles.clear()
            game.powerups.clear()
            decode = copyDecode.copy()
            startGameTime = time.time()
            mixer.music.play()

        pygame.display.update()
        clock.tick(120)
