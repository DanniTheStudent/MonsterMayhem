import pygame
import sys
pygame.init()
pygame.font.init()

coins = 0

font = pygame.font.SysFont('Raider', 25)
coin_font = pygame.font.SysFont('Raider', 35)
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

apple_x = 20
apple_y = 30
apple_text = font.render('Apple', True, (250, 250, 250))
apple_rect = apple_x, apple_y

tomato_x = 170
tomato_y = 30
tomato_text = font.render('Tomato', True, (250, 250, 250))
tomato_rect = tomato_x, tomato_y

ham_x = 320
ham_y = 30
ham_text = font.render ('Ham', True, (250, 250, 250))
ham_rect = ham_x, ham_y

sushi_x = 440
sushi_y = 30
sushi_text = font.render ('Sushi', True, (250, 250, 250))
sushi_rect = sushi_x, sushi_y

pizza_x = 560
pizza_y = 30
pizza_text = font.render ('Pizza', True, (250, 250, 250))
pizza_rect = pizza_x, pizza_y

mini_ring_x = 20
mini_ring_y = 150
mini_ring_text = font.render ('Mini ring', True, (250, 250, 250))
mini_ring_rect = mini_ring_x, mini_ring_y

medium_ring_x = 170
medium_ring_y = 150
medium_ring_text = font.render ('Medium ring', True, (250, 250, 250))
medium_ring_rect = medium_ring_x, medium_ring_y

power_ring_x = 320
power_ring_y = 150
power_ring_text = font.render ('Power ring', True, (250, 250, 250))
power_ring_rect = power_ring_x, power_ring_y

mythical_ring_x = 440
mythical_ring_y = 150
mythical_ring_text = font.render ('Mythical ring', True, (250, 250, 250))
mythical_ring_rect = mythical_ring_x, mythical_ring_y

supreme_ring_x = 560
supreme_ring_y = 150
supreme_ring_text = font.render ('Supreme ring', True, (250, 250, 250))
supreme_ring_rect = supreme_ring_x, supreme_ring_y

lens_x = 20
lens_y = 270
lens_text = font.render ('Lens', True, (250, 250, 250))
lens_rect = lens_x, lens_y

vial_x = 20
vial_y = 390
vial_text = font.render ('Vial', True, (250, 250, 250))
vial_rect = vial_x, vial_y

shopping_cart_x = 600
shopping_cart_y = 450
shopping_cart_rect = shopping_cart_x, shopping_cart_y

back_arrow_x = 600
back_arrow_y = 450
back_arrow_rect = back_arrow_x, back_arrow_y

messages = ["Buy now?", "Not enough coins!", "Item purchased!", "Too many items in cart."]
message_x = 300
message_y = 400
message_1 = font.render ( f"{messages[0]}", True, (250, 250, 250))
message_2 = font.render ( f"{messages[1]}", True, (250, 250, 250))
message_3 = font.render ( f"{messages[2]}", True, (250, 250, 250))
message_4 = font.render ( f"{messages[3]}", True, (250, 250, 250))

coin_text_x = 300
coin_text_y = 300

shop_background = pygame.transform.scale (pygame.image.load("sprites/shop/shop.jpg"), (WIDTH, HEIGHT))
shop_x = 0
shop_y = 0

item_is_available = False
show_message = False
message_timer = 5000

number_of_items = 0

text_was_selected = False

SHOP_SCREEN = 0
CART_SCREEN = 1
current_screen = SHOP_SCREEN
current_items = []
class Item:

    def __init__(self, name, cost, image_path, position):
        self.name = name
        self.cost = cost
        self.image = pygame.transform.scale(pygame.image.load(image_path), (WIDTH // 10, HEIGHT // 10))
        self.rect = self.image.get_rect(topleft=position)
        self.text = font.render(name, True, (250, 250, 250))
        self.text_rect = self.text.get_rect(topleft=(position[0], position[1] + 60))

class shopping_cart:

    def __init__(self, name, image_path, position):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(image_path), (WIDTH // 10, HEIGHT // 10))
        self.rect = self.image.get_rect(topleft=position)
        self.text = font.render(name, True, (250, 250, 250))
        self.text_rect = self.text.get_rect(topleft=(position[0], position[1] + 60))

class back_arrow:

    def __init__(self, name, image_path, position):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(image_path), (WIDTH // 10, HEIGHT // 10))
        self.rect = self.image.get_rect(topleft=position)
        self.text = font.render(name, True, (250, 250, 250))
        self.text_rect = self.text.get_rect(topleft=(position[0], position[1] + 60))

class Gameplay:
    def __init__(self, character):
        self.coins = character.purse
        self.current_items = []
        self.message_timer = 5000
        self.show_message = False
        self.item_is_available = False
        self.number_of_items = 0
        self.font = pygame.font.SysFont('Raider', 25)
        self.WIDTH, self.HEIGHT = 640, 480
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.selected_item = None
        self.current_screen = SHOP_SCREEN
        self.back_arrow_clicked = False
        self.character = character

#damage, energy, defense
        self.items = [
            Item("Tomato", 2, "sprites/shop/tomato.png", (20, 30)),
            Item("Apple", 5, "sprites/shop/apple.png", (270, 30)),
            Item("Pizza", 10, "sprites/shop/pizza.png", (560, 30)),
            Item("Mini ring", 10, "sprites/shop/ring_01.png", (20, 150)),
            Item("Mythical ring", 12, "sprites/shop/ring_03.png", (270, 150)),
            Item("Supreme ring", 15, "sprites/shop/ring_04.png", (560, 150)),
            Item("Contact lenses", 10, "sprites/shop/lens1.jpg", (20, 270)),
            Item("Adrenaline boost", 7, "sprites/shop/vial.png", (20, 370)),
        ]

        self.cart = shopping_cart ("View current items", "sprites/shop/shopping_cart.png", (450, 400))
        self.arrow = back_arrow("Back", "sprites/shop/back.png", (450, 300))

    
    def handle_shopping_cart_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.cart.rect.collidepoint(event.pos) and self.current_screen == SHOP_SCREEN:
                self.show_current_items_screen()
    
    def handle_back_arrow_click(self, event):
        if self.current_screen == CART_SCREEN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.arrow.rect.collidepoint(event.pos):
                    self.back_arrow_clicked = True
    
    def show_current_items_screen(self):
        self.current_screen = CART_SCREEN

    def event_handling(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for item in self.items:
                if item.rect.collidepoint(event.pos):
                    self.select_item(item)

    def select_item(self, item):
        if self.coins >= item.cost:
            self.show_message = True
            self.item_is_available = True
            self.selected_item = item
        else:
            self.show_message = True
            self.item_is_available = False

    def run(self, character):
        running = True
        while running:
            self.screen.fill((255, 255, 255))

            self.coin_text = coin_font.render (f"Coins: {character.purse}", True, (250, 250, 250))

            for event in pygame.event.get():
                self.event_handling(event)
                self.handle_shopping_cart_click(event) 
                self.handle_back_arrow_click(event)

            if self.current_screen == CART_SCREEN:
                self.screen.fill ((137, 207, 240))
                self.screen.blit(self.arrow.image, self.arrow.rect.topleft)
                self.screen.blit(self.arrow.text, self.arrow.text_rect.topleft)
                
                for item_name in self.current_items:
                    for item in self.items:
                        if item.name == item_name:
                            self.screen.blit(item.image, item.rect.topleft)
                            self.screen.blit(item.text, item.text_rect.topleft)
                            cost_text = font.render(f"Cost: {item.cost}", True, (250, 250, 250))
                            self.screen.blit(cost_text, (item.text_rect.x, item.text_rect.y + 20))

            elif self.current_screen == SHOP_SCREEN:

                self.screen.blit(shop_background, (shop_x, shop_y))

                self.screen.blit(self.coin_text, (coin_text_x, coin_text_y))

                for item in self.items:
                    self.screen.blit(item.image, item.rect.topleft)
                    self.screen.blit(item.text, item.text_rect.topleft)
                    cost_text = font.render(f"Cost: {item.cost}", True, (250, 250, 250))
                    self.screen.blit(cost_text, (item.text_rect.x, item.text_rect.y + 20))

                self.screen.blit(self.cart.image, self.cart.rect.topleft)
                self.screen.blit(self.cart.text, self.cart.text_rect.topleft)

# Add character as a parameter in class, character.inventroy.append
                if self.show_message:
                    if self.item_is_available:
                        self.screen.blit(message_1, (message_x, message_y))

                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if (
                            message_x <= mouse_x <= message_x + message_1.get_width() and
                            message_y <= mouse_y <= message_y + message_1.get_height()
                        ):
                            if pygame.mouse.get_pressed()[0] and number_of_items <= 3:
                                self.current_items.append(self.selected_item.name)
                                self.character.inventory.append(self.selected_item.name)
                                self.coins -= self.selected_item.cost
                                self.show_message = False
                                self.screen.blit(message_3, (message_x, message_y))
                                self.number_of_items += 1

                                if self.number_of_items > 3:
                                    self.screen.blit(message_4, (message_x, message_y))

                    else:
                        self.screen.blit(message_2, (message_x, message_y))
                        self.message_timer -= 1

                    if self.message_timer <= 0:
                        self.show_message = False
                        self.message_timer = 5000
            
            if self.back_arrow_clicked:
                self.current_screen = SHOP_SCREEN  
                self.back_arrow_clicked = False
            
            pygame.display.flip()


def main(player_character):
    shop_game = Gameplay(player_character)
    shop_game.run(player_character)
