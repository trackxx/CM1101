import weapons
from items import *
from map import rooms

inventory = []
active_weapons = [weapons.weapon_fists, weapons.weapon_foot]
current_weapon = weapons.weapon_fists
current_room = rooms["Toilet"]
health = 100
drunk = 90
money = 0
name = ""
start_time = 0
end_time = 0
completion = False
