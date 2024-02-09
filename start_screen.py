import pygame

pygame.init()

# Screen dimensions
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def title_screen():
    # ---------------------------
    # Initialize global variables

    player = 1

    location = "title_screen"



    # Image, backgrounds & sprites load
    background = pygame.transform.scale (pygame.image.load("sprites/title_screen/background.jpg"), (WIDTH, HEIGHT))
    title = pygame.transform.scale (pygame.image.load("sprites/title_screen/title.png"), (270, 129))
    start = pygame.transform.scale (pygame.image.load("sprites/title_screen/start.png"), (130, 30))
    quit = pygame.transform.scale (pygame.image.load("sprites/title_screen/quit.png"), (126, 34))
    red_start = pygame.transform.scale (pygame.image.load("sprites/title_screen/red-start.png"), (130, 30))
    red_quit = pygame.transform.scale (pygame.image.load("sprites/title_screen/red-quit.png"), (126, 34))
    brown_bacground = pygame.transform.scale(pygame.image.load("sprites/title_screen/brown_background.jpg"), (WIDTH, HEIGHT))
    left_arrow = pygame.transform.scale(pygame.image.load("sprites/title_screen/left_arrow.png"), (42,48))
    right_arrow = pygame.transform.scale(pygame.image.load("sprites/title_screen/right_arrow.png"), (42, 48))
    left_arrow_select = pygame.transform.scale(pygame.image.load("sprites/title_screen/left_arrow_select.png"),(42, 48))
    right_arrow_select = pygame.transform.scale(pygame.image.load("sprites/title_screen/right_arrow_select.png"),(42, 48))
    charecter_frame = pygame.transform.scale(pygame.image.load("sprites/title_screen/charecter_frame.png"),(200, 200))
    select_button = pygame.transform.scale(pygame.image.load("sprites/title_screen/select_button.png"), (104, 22))
    select_button_red = pygame.transform.scale(pygame.image.load("sprites/title_screen/red_select_button.png"),(104, 22))
    bladekeeper = pygame.transform.scale(pygame.image.load("sprites/title_screen/bladekeeper.png"),(88, 84))
    fire_knight = pygame.transform.scale(pygame.image.load("sprites/title_screen/fire_knight.png"),(120, 88))
    leaf_ranger = pygame.transform.scale(pygame.image.load("sprites/title_screen/leaf_ranger.png"),(98, 88))
    ground_monk = pygame.transform.scale(pygame.image.load("sprites/title_screen/ground_monk.png"),(72, 102))
    back = pygame.transform.scale(pygame.image.load("sprites/title_screen/back.png"), (66, 22))
    red_back = pygame.transform.scale(pygame.image.load("sprites/title_screen/red_back.png"), (66, 22))
    bladekeeper_title = pygame.transform.scale(pygame.image.load("sprites/title_screen/bladekeeper_title.png"), (94, 50))
    fire_knight_title = pygame.transform.scale(pygame.image.load("sprites/title_screen/fire_knight_title.png"), (110, 50))
    leaf_ranger_title = pygame.transform.scale(pygame.image.load("sprites/title_screen/leaf_ranger_title.png"), (104, 50))
    ground_monk_title = pygame.transform.scale(pygame.image.load("sprites/title_screen/ground_monk_title.png"), (110, 50))




    running = True
    while running:

    # Title screen display
        if location == "title_screen":

    # Buttons & background
            start_box = pygame.draw.rect(screen, (0, 0, 0), (255, 220, 130, 30))
            quit_box = pygame.draw.rect(screen, (0, 0, 0), (257, 275, 126, 34))
            screen.blit(background, (0, 0))

    # Button sprites & other
            screen.blit(title, (185, 50))
            screen.blit(start, (255, 225))
            screen.blit(quit, (257, 275))

    # Colour change if touching button
            if start_box.collidepoint(pygame.mouse.get_pos()):
                screen.blit(red_start, (255, 225))
            elif quit_box.collidepoint(pygame.mouse.get_pos()):
                screen.blit(red_quit, (257, 275))

    # Events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_box.collidepoint(event.pos) and pygame.MOUSEBUTTONDOWN:
                        exit()
                    if start_box.collidepoint(event.pos) and pygame.MOUSEBUTTONDOWN:
                        location = "charecter_select"

    # charecter select display
        elif location == "charecter_select":


     # Background & buttons
            left_box = pygame.draw.rect(screen, (0, 0, 0), (150, 220, 42, 48))
            right_box = pygame.draw.rect(screen, (0, 0, 0), (450, 220, 42, 48))
            select_box = pygame.draw.rect(screen, (0, 0, 0), (268, 360, 104, 22))
            back_box = pygame.draw.rect(screen, (0, 0, 0), (287, 400, 66, 33))
            screen.blit(brown_bacground, (0, 0))

    # Button sprites & other
            screen.blit(charecter_frame, (220, 140))
            screen.blit(right_arrow, (450, 220))
            screen.blit(left_arrow, (150, 220))
            screen.blit(select_button, (268, 360))
            screen.blit(back, (287, 400))

    # Colour change if touching button
            if left_box.collidepoint(pygame.mouse.get_pos()):
                screen.blit(left_arrow_select, (150, 220))

            elif right_box.collidepoint(pygame.mouse.get_pos()):
                screen.blit(right_arrow_select, (450, 220))

            elif select_box.collidepoint(pygame.mouse.get_pos()):
                screen.blit(select_button_red, (268, 360))

            elif back_box.collidepoint(pygame.mouse.get_pos()):
                screen.blit(red_back, (287, 400))

    # Charecter scroll
            if player == 0:
                player = 4
            elif player == 5:
                player = 1
            elif player == 1:
                screen.blit(bladekeeper, (276, 198))
                screen.blit(bladekeeper_title, (273, 50))
            elif player == 2:
                screen.blit(fire_knight, (260, 196))
                screen.blit(fire_knight_title, (265, 50))
            elif player == 3:
                screen.blit(leaf_ranger, (271, 196))
                screen.blit(leaf_ranger_title, (268, 50))
            elif player == 4:
                screen.blit(ground_monk, (284, 189))
                screen.blit(ground_monk_title, (265, 50))

    # Events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_box.collidepoint(event.pos):
                        location = "title_screen"
                    elif left_box.collidepoint(event.pos):
                        player -= 1
                    elif right_box.collidepoint(event.pos):
                        player += 1
                    elif select_box.collidepoint(event.pos):
                        return (player, 1)



# Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False





        pygame.display.flip()
        clock.tick(30)
        #---------------------------
    return (player, 1)

if __name__ == "__main__":
    title_screen()
