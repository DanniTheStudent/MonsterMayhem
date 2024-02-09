import os
import sys

import pygame

import status_bar

sys.path.append("characters")
sys.path.append("buttons")

import atk_buttons
import stage_change_buttons
import character_class as cc
import monsters
import player_characters
import shop

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()




def main(current_character, room, high_score):
    pygame.font.init()
    font = pygame.font.SysFont("Impact", 20)
    
    
    battling = True
    new_state = None

    backround = pygame.image.load("sprites/background_mayhem.png")

    # ---------------------------
    # Initialize global variables
    for item in current_character.inventory:
        current_character.MAX_HEALTH += item.cost
        current_character.MAX_ENERGY += item.cost
        for attack in current_character.moveset:
            attack.damage += item.cost
        current_character.total_stat_buff += item.cost
        current_character.inventory.remove(item)
    current_character.get_animations_sprite_sheet("sprite_sheet.png")

    current_character.energy = (current_character.MAX_ENERGY // 4) * 3
    current_character.health = current_character.MAX_HEALTH

    character_healthbar = status_bar.Bar(current_character.MAX_HEALTH, 15, 170, 375, (200,0,0))
    character_energybar = status_bar.Bar(current_character.MAX_ENERGY, 15, 170, 395, (0,0,200))

    current_purse = font.render(f"Purse: {current_character.purse}", True, (255,255,255))
    current_score = font.render(f"Score: {current_character.score}", True, (255,255,255))

    high_score_text = font.render(f"High Score: {high_score}", True, (255,255,255))

    current_enemy = monsters.list[room.enemy_num]
    current_enemy.current_action = 0
    current_enemy.current_animation = 0
    for animation in os.listdir(f"sprites/{current_enemy.name}"):
        current_enemy.get_animations_sprite_sheet(animation)

    current_enemy.MAX_HEALTH = int(round(current_enemy.MAX_HEALTH * room.enemy_multiplier))
    current_enemy.health = current_enemy.MAX_HEALTH
    
    
    current_enemy.moveset[0].damage = int(round(current_enemy.moveset[0].damage * room.enemy_multiplier))

    enemy_healthbar = status_bar.Bar(current_enemy.MAX_HEALTH, 20, 330, 50, (200,0,0))
    
    frame_counter = 0

    for button in atk_buttons.list:
        button.get_animations_png()
    for button in stage_change_buttons.list:
        button.get_animations_png()

    stage_change_buttons.quit_button.get_animations_png()
    # ---------------------------

    running = True
    
    while running:
        # EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 
                  and current_character.current_animation == 0):
                if stage_change_buttons.quit_button.check_for_cursor():
                    stage_change_buttons.quit_button.state = True
                elif battling is True:
                    for button in atk_buttons.list:
                        if (button.check_for_cursor() and 
                        current_character.moveset[atk_buttons.list.index(button)].stamina_cost <= current_character.energy):
                            button.state = True
                            break
                elif battling is False:
                    for button in stage_change_buttons.list:
                        if button.check_for_cursor():
                            button.state = True
                            break

        # GAME STATE UPDATES
        # All game math and comparisons happen here

        if stage_change_buttons.quit_button.state is True:
            running = False
            stage_change_buttons.quit_button.state = False
            new_state = 4
            break
        


        if current_enemy.health <= 0 and battling == True:
            battling = False
            current_character.purse += room.gold_gained
            current_character.score += room.room_id


        if battling is False:
            if stage_change_buttons.list[0].state is True:
                running = False
                new_state = 1
            elif stage_change_buttons.list[1].state is True:
                running = False
                new_state = 2

            for button in stage_change_buttons.list:
                button.state = False

            if new_state is not None:
                break

        stage_change_buttons.quit_button.update()
        
        if battling is True:
            cc.action_sequence(current_character, current_enemy)
            for button in atk_buttons.list:
                button.update()
            character_healthbar.update(current_character.health)
            character_energybar.update(current_character.energy)
            enemy_healthbar.update(current_enemy.health)
            current_character.button_check(current_enemy, atk_buttons.list)
            current_enemy.update(frame_counter)
        
        elif battling is False:
            for button in stage_change_buttons.list:
                button.update()

        current_character.update(frame_counter)
        current_purse = font.render(f"Purse: {current_character.purse}", True, (255,255,255))
        current_score = font.render(f"Score: {current_character.score}", True, (255,255,255))
        if high_score < current_character.score:
            high_score = current_character.score
        high_score_text = font.render(f"High Score: {high_score}", True, (255,255,255))


        
        
        frame_counter += 1


        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command
        screen.blit((backround), (0, 0))
        current_character.draw(screen)
        screen.blit(current_purse, (180, 10))
        screen.blit(current_score, (290, 10))
        screen.blit(high_score_text, (400, 10))
        stage_change_buttons.quit_button.draw(screen)

        if battling is True:
            current_enemy.draw(screen)
            character_healthbar.draw(screen)
            character_energybar.draw(screen)
            enemy_healthbar.draw(screen)
            for button in atk_buttons.list:
                button.draw(screen)

        elif battling is False:
            for button in stage_change_buttons.list:
                button.draw(screen)

        if current_character.health <= 0:
            new_state = 3
            break

        # Must be the last two lines
        # of the game loop
                

        pygame.display.flip()
        clock.tick(30)

        #---------------------------
    

    room.update()

    room.room = room
    return (new_state, high_score)
