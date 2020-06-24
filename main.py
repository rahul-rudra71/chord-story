import pygame, os, sys
from pygame.locals import *
from Obstacle import Obstacle

os.environ['SDL_AUDIODRIVER'] = 'dsp'

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Chord Story')

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window

display = pygame.Surface((300, 200))  # used as the surface for rendering, which is scaled




#grass_img = pygame.image.load('grass.png')
#dirt_img = pygame.image.load('dirt.png')


chord = pygame.image.load('mainmenu.png')
#menu_size = menu.get_size()
#menu_rect = menu.get_rect()


background = pygame.image.load('background.png')
background_size = background.get_size()
background_rect = background.get_rect()
w, h = background_size
x = 0
y = 0
x1 = 0
y1 = -h

scroll = 1

obstacles = []

running = True

click = False

def main_menu():
    menu_open = True
    while menu_open:
        
        display.fill((255, 255, 255))  # clear screen by filling it with white
        
        screen.blit(chord, (0,0))
        
        
        
        
        mousex, mousey = pygame.mouse.get_pos()
        
        # create the classic mode button
        classic_button = pygame.Rect(50,50, 150, 60)
        
        if classic_button.collidepoint((mousex, mousey)):
            if(click):
                # play the game if the button is pressed
                run_game()
        
        # render button
        pygame.draw.rect(screen, (156, 17, 21), classic_button)
        
        classic_font = pygame.font.Font('freesansbold.ttf', 17)
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


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]

    if rect.right > 299:
        rect.right = 299
    if rect.x < 0:
        rect.x = 0

    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        # elif movement[1] < 0:
        #     rect.top = tile.bottom
        #     collision_types['top'] = True
    return rect, collision_types


def obstacle_collision(player, obstacles):
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            return False
        if obstacle.rect.left < -15:
            obstacles.remove(obstacle)
    return True


def game_over():
    font = pygame.font.Font('freesansbold.ttf', 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)


NEWOBSTACLE = USEREVENT + 1
pygame.time.set_timer(NEWOBSTACLE, 500)

def run_game():
    play_game = True
    running = True
    
    
    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    true_scroll = [0, 0]
    
    player_img = pygame.image.load('player.png').convert()
    player_img.set_colorkey((255, 255, 255))

    player_rect = pygame.Rect(100, 100, 5, 13)
    
    
    while play_game:  # game loop
        display.fill((255, 255, 255))  # clear screen by filling it with white

        # scrolling background
        display.blit(background, background_rect)  # left image
        display.blit(background, background_rect.move(background_rect.width, 0))  # right image
        if running:
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

        for obstacle in obstacles:
            if running:
                obstacle.rect.x -= 2
            pygame.draw.rect(display, (255, 255, 255), obstacle.rect)

        player_movement = [0, 0]

        if running:
            if moving_right == True:
                player_movement[0] += 2
            if moving_left == True:
                player_movement[0] -= 2
            player_movement[1] += vertical_momentum
            vertical_momentum += 0.2
            if vertical_momentum > 3:
                vertical_momentum = 3

        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        running = obstacle_collision(player_rect, obstacles)

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                running = False
                play_game = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and running:
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
                    player_rect.y += 12
                    if player_rect.y > 166:
                        player_rect.y = 166
            if event.type == KEYUP and running:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
            if event.type == NEWOBSTACLE:
                obstacle = Obstacle()
                obstacles.append(obstacle)

        if running:
            player_rect.x -= scroll

        display.blit(player_img, (player_rect.x, player_rect.y))

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

        if not running:
            game_over()

        pygame.display.update()
        clock.tick(60)
        
main_menu()
