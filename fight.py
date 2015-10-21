import player
import time
from people import *
from weapons import *

def weapon_selection(index):
    for i in range(0, len(player.active_weapons)):
        print("Press " + str(i + 1) + " to choose " + player.active_weapons[i]["name"] + " as your Weapon")
    choice = int(input())
    player.current_weapon = player.active_weapons[(choice - 1)]
    print_fight_menu(index)

def use_item():
    '''Use items to regain health and inflict damage to your opponent'''
    pass

def attack_enemy(index):
    print("You attacked " + index["name"] + " with your " + player.current_weapon["name"])
    print("You inflicted " + str(player.current_weapon["damage"]) + " damage!")
    index["health"] -= player.current_weapon["damage"]
    time.sleep(3)
    if index["health"] <= 0:
        print("You killed " + index["name"] + "!")
        time.sleep(2)
        return True
    print(index["name"] + " attacked you with " + index["weapon"]["name"])
    print("You lost " + str(index["weapon"]["damage"]) + " health!\n")
    player.health -= index["weapon"]["damage"]
    time.sleep(3)
    if player.health <= 0:
        print("You have been killed.")
        time.sleep(3)
        return False
    return True

def print_fight_stats(index):
    print("You Are Fighting " + index["name"])
    print("Their Health: " + str(index["health"]))
    print("Your Health: " + str(player.health))
    print("Your Weapon: " + player.current_weapon["name"])

def print_fight_menu(index):
    print_fight_stats(index)
    return int(input("\nPress 1 for Weapon Selection\nPress 2 to Use Item\nPress 3 to Attack Enemy\n"))

def fight_scene(index):
    alive = True
    while alive:
        choice = print_fight_menu(index)
        if choice == 1:
            weapon_selection(index)
        elif choice == 2:
            use_item()
        elif choice == 3:
            if attack_enemy(index):
                if index["health"] <= 0:
                    alive = False
            else:
                alive = False
