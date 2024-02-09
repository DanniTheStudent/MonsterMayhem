import pygame
import room

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

def death_screen():
    room.room = room.starting_room
    death_screen = pygame.transform.scale(pygame.image.load(r"sprites/death_screen.png"), SIZE)
    restart = pygame.transform.scale(pygame.image.load("sprites/restart.png"), (128, 22))
    restart_red = pygame.transform.scale(pygame.image.load("sprites/restart_red.png"), (128, 22))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_box.collidepoint(event.pos):
                    return 0

        restart_box = pygame.draw.rect(screen, (0, 0, 0), (256, 300, 128, 22))
        screen.blit(death_screen, (0, 0)) 
        screen.blit(restart, (256, 300))
        
        if restart_box.collidepoint(pygame.mouse.get_pos()):
            screen.blit(restart_red, (256, 300))
            
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    death_screen()
