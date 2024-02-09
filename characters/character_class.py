import pygame
import os
import numpy as np


# D. Klich - template for characters in the game
class Character(pygame.sprite.Sprite):
    def __init__ (self, name : str, health : int, energy : int, moveset : list,
                 coordinates : tuple, sprite_width : int, sprite_height : int, attack_animation_start_index = 0):
        super().__init__()
        self.user_name = None
        self.name = name
        self.MAX_HEALTH = health
        self.health = health
        self.MAX_ENERGY = energy
        self.energy = energy
        self.moveset = moveset
        self.purse = 0
        self.score = 0
        self.total_stat_buffs = 0
        self.inventory = []
        self.attacking = False
        self.current_action = None

        self.animations = []
        self.current_animation = 0
        self.previous_animation = self.current_animation
        self.animation_frame_number = 0
        self.image = pygame.surface.Surface((sprite_width, sprite_height))
        self.rect = self.image.get_rect()
        self.start_coordinates = coordinates
        self.rect.topleft = self.start_coordinates

        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.animation_speed = 5
        self.attack_animation_start_index = attack_animation_start_index

        # Chat GPT assistance
    def check_blank_frame(self, frame : pygame.surface.SurfaceType):
        alpha_values = pygame.surfarray.pixels_alpha(frame)
        if np.all(alpha_values <= 0):
            return True

        return False

    # Stack Overflow assistance
    def get_frame(self, position_x, position_y, width, height, sprite_sheet):
        frame = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        frame.blit(sprite_sheet, (0, 0), (position_x, position_y, width, height))
        frame.convert_alpha()

        return frame

    # Gets Sprite Sheet and loops through it
    def get_animations_sprite_sheet(self, sprite_sheet_name : str) -> None:
        sprite_sheet = pygame.image.load(f"sprites/{self.name}/{sprite_sheet_name}")
        rows = sprite_sheet.get_height() // self.sprite_height
        columns = sprite_sheet.get_width() // self.sprite_width

        for row in range(rows):
            animation = []
            for column in range(columns):
                frame = (self.get_frame(column * self.sprite_width, row * self.sprite_height, self.sprite_width, self.sprite_height, sprite_sheet))
                if self.check_blank_frame(frame) is True:
                    break
                animation.append(frame)
            self.animations.append(animation)


    def get_animations_png(self) -> None:
        for animation in os.listdir(f"sprites/{self.name}"):
            frames = []
            if int(animation[0]) is not ValueError:
                for frame in os.listdir(f"sprites/{self.name}/{animation}"):
                    frame = pygame.image.load(f"{self.name}/{animation}/{frame}").convert_alpha()
                    frames.append(frame)
                    self.animations.append(frames)

    def draw(self, screen : pygame.surface.SurfaceType) -> None:
        screen.blit(self.image, self.rect)


    def update(self, frame_counter : int):
        if frame_counter % self.animation_speed == 0:
            self.animation_frame_number += 1
            if self.animation_frame_number == len(self.animations[self.current_animation]):
                self.animation_frame_number = 0
                if self.current_animation != 0:
                    self.current_animation = 0

        if self.current_animation != self.previous_animation:
            self.animation_frame_number = 0


        self.image = self.animations[self.current_animation][self.animation_frame_number]
        self.previous_animation = self.current_animation

        if self.current_animation != 0:
            self.attacking = True
        else:
            self.attacking = False

            

        

    def button_check(self, enemy, buttons : list):
        for button in buttons:
            if button.state is True and self.energy - self.moveset[buttons.index(button)].stamina_cost >= 0:
                self.current_animation = buttons.index(button) + self.attack_animation_start_index
                if self.animation_frame_number == len(self.animations[self.current_animation]) - 1:
                    button.state = not button.state
                    self.current_action = buttons.index(button)
                    enemy.current_animation = -1

def action_sequence(player, enemy):
    if player.current_action is not None and enemy.attacking is True:
        player_damage = player.moveset[player.current_action].damage - enemy.moveset[0].defense
        enemy_damage = enemy.moveset[0].damage - player.moveset[player.current_action].defense
        energy_cost = player.moveset[player.current_action].stamina_cost

        
        if player_damage < 0:
            player_damage = 0
        if enemy_damage < 0:
            enemy_damage = 0

        enemy.health -= player_damage
        player.health -= enemy_damage
        player.energy -= energy_cost
        
        player.current_action = None
        player.energy += player.MAX_ENERGY // 10
        if player.energy > player.MAX_ENERGY:
            player.energy = player.MAX_ENERGY
        
        
        
        
            
            

            
# Gleb G. - charachters' actions in the game
class Actions:
    def __init__(self, name : str, damage : int, defense : int, stamina_cost: int,
                 self_status_effect : object, enemy_status_effect : object) -> None:
        self.name = name
        self.damage = damage
        self.defense = defense
        self.ally_status_effect = self_status_effect
        self.enemy_status_effect = enemy_status_effect
        self.stamina_cost = stamina_cost

def attacks() -> list:
    regular_attack = Actions('regular attack', 10, 10, 0, None, None)
    charged_attack = Actions('charged attack', 25, 0, 0, None, None)
    special_attack_1 = Actions('special attack 1', 40, 10, 20, None, None)
    special_attack_2 = Actions('special attack 2', 70, 20, 40, None, None)
    return [regular_attack, charged_attack, special_attack_1, special_attack_2]

# Gleb G. - weapons' effects
class Effects:
    def __init__(self, name: str, damage: int, healing: int, duration: int) -> None:
        self.name = name
        self.type = type
        self.damage = damage
        self.healing = healing
        self.duration = duration
