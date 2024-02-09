#Gleb G. - levels
class Levels:
    def __init__(self):
        self.room_id = 1
        self.enemy_num = 0
        self.enemy_multiplier = 1
        self.gold_gained = 10

    #stack overflow and chatgpt assistance 
    def update(self):
        self.room_id += 1
        self.enemy_num = (self.room_id - 1) % 5
        self.enemy_multiplier = ((((self.room_id- 1) // 5) * 5) / 10) + 1
        self.gold_gained = int (10 * ((1 + (self.room_id - 1) / 10)))
        
room = Levels()
starting_room = Levels()
        
