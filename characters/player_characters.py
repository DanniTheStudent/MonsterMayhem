# Gleb
import character_class as cc

bladekeeper_moveset = cc.attacks()
fireknight_moveset = cc.attacks()
ground_monk_moveset = cc.attacks()
leaf_ranger_moveset = cc.attacks()

player_coordinates = (-87, 60)

bladekeeper = cc.Character("bladekeeper", 60, 90, bladekeeper_moveset, 
                          player_coordinates, 432, 192, 9)  
fireknight = cc.Character('fire knight', 100, 50, fireknight_moveset, 
                         player_coordinates, 432, 192, 7)  
ground_monk = cc.Character('ground monk', 75, 75, ground_monk_moveset, 
                          player_coordinates, 432, 192, 5) 
leaf_ranger = cc.Character('leaf ranger', 90, 60, leaf_ranger_moveset, 
                          player_coordinates, 432, 192, 11)

list = [bladekeeper, fireknight, leaf_ranger, ground_monk]
