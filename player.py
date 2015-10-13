from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
# Start game at the reception
current_room = rooms["Reception"]
health = 100
armour = 0
# possibly add exp to increase health and level
experience = 0
level = 1