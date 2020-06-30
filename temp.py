def select_difficulty():
    click = 0
    select = True
    while select:
        display.fill((224, 132, 132))  # clear screen by filling it with pink

        screen.blit(pinkbackground, (0, 0))

        font = pygame.font.Font('freesansbold.ttf', 45)
        font2 = pygame.font.Font('freesansbold.ttf', 45)
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

        if easy_button.collidepoint((mousex, mousey)):
            if (click):
                difficulty = 0.25
                select = False
        if medium_button.collidepoint((mousex, mousey)):
            if (click):
                difficulty = 0.35
                select = False
        if hard_button.collidepoint((mousex, mousey)):
            if (click):
                difficulty = 0.5
                select = False

        # render buttons
        pygame.draw.rect(screen, (255, 255, 255), easy_button)
        pygame.draw.rect(screen, (255, 255, 255), medium_button)
        pygame.draw.rect(screen, (255, 255, 255), hard_button)

        # easy text
        font = pygame.font.Font('freesansbold.ttf', 35)
        font2 = pygame.font.Font('freesansbold.ttf', 35)
        text = font.render("EASY", True, (0, 0, 0))
        text2 = font.render("EASY", True, (224, 132, 132))
        screen.blit(text, (247,116))
        screen.blit(text2, (249, 118))

        # medium text
        font = pygame.font.Font('freesansbold.ttf', 30)
        font2 = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("MEDIUM", True, (0, 0, 0))
        text2 = font.render("MEDIUM", True, (224, 132, 132))
        screen.blit(text, (237,216))
        screen.blit(text2, (239, 218))

        # hard text
        font = pygame.font.Font('freesansbold.ttf', 35)
        font2 = pygame.font.Font('freesansbold.ttf', 35)
        text = font.render("HARD", True, (0, 0, 0))
        text2 = font.render("HARD", True, (224, 132, 132))
        screen.blit(text, (247,316))
        screen.blit(text2, (249, 318))

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