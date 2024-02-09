import pygame
import start_screen # includes character selection
import battle
import shop
import death_screen
import json

import sys
import room

sys.path.append("characters")

import player_characters

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()


current_screen = 0  
current_character = 0
high_score = 0 

def load_high_score():
    try:
        with open("high_score.json", "r") as json_file:
            highest_level = json.load(json_file)
            return highest_level.get("new_high_score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0
    
def save_high_score(high_score):
    loaded_high_score = load_high_score()

    if high_score > loaded_high_score:
        highest_level = {"new_high_score" : high_score}
        
        try:
            with open("high_score.json", "w") as json_file:
                json.dump(highest_level, json_file)
        except Exception as e:
            print(f"Error saving high score: {e}")

    return loaded_high_score





#Gleb G. - game screens
def main():
    global current_screen
    global high_score
    global current_character

    high_score = load_high_score()

    while True:
        if current_screen == 0:
            current_screen = start_screen.title_screen()#INCLUDES CHARACTER SELECTION
            current_character = player_characters.list[current_screen[0] -1]
            current_screen = current_screen[1]
        elif current_screen == 1: #battle screen
            current_screen = battle.main(current_character, room.room, high_score)
            high_score = current_screen[1]
            current_screen = current_screen[0]  
            save_high_score(high_score)

        elif current_screen == 2: #shop
            current_screen = shop.main(current_character)                   
            
        elif current_screen == 3: #death screen
            current_character.score = 0
            current_character.purse = 0
            current_screen = death_screen.death_screen()

        elif current_screen == 4: # quit game
            pygame.quit()
            break

if __name__ == '__main__':
    main()
