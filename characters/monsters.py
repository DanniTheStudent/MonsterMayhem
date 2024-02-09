# Gleb
import character_class as cc

demon_attack = cc.Actions('demon_attack', 25, 0, 0,None, None)

fire_skull_attack = cc.Actions('fire_skull_attack', 12, 0, 0, None, None)

ghost_attack = cc.Actions('ghost_attack', 10, 0, 0, None, None)

nightmare_attack = cc.Actions('nightmare_attack', 15, 0, 0, None, None)

hell_beast_attack = cc.Actions('hell_beast_attack', 20, 0, 0, None, None)

demon = cc.Character('demon', 200, 0, [demon_attack], (370,-30), 384, 352)
fire_skull = cc.Character('fire skull', 100, 0, [fire_skull_attack], (450,40), 144, 168)
ghost = cc.Character('ghost', 75, 0, [ghost_attack], (455,110), 128, 160)
nightmare = cc.Character('nightmare', 150, 0, [nightmare_attack], (400,65), 256, 192)
hell_beast = cc.Character('hell beast', 125, 0, [hell_beast_attack], (450,130), 128, 128)

list = [ghost, fire_skull, hell_beast, nightmare, demon]
