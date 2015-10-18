import weapons
from items import *
from map import rooms

inventory = []
active_weapons = [weapons.weapon_fists, weapons.weapon_pistol]
current_weapon = weapons.weapon_fists
current_room = rooms["Factory Floor"]
health = 100
armour = 0
mass = 0
experience = 0
level = 1
# character = ""
name = ""
gender = ""
start_time = 0
end_time = 0
completion = False
