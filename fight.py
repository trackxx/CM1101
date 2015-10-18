import player
import time
from enemy import *
from weapons import *

def weapon_selection():
    for i in range(0, len(player.active_weapons)):
        print("Press " + str(i + 1) + " to choose " + player.active_weapons[i]["name"] + " as your Weapon")
    choice = int(input())
    player.current_weapon = player.active_weapons[(choice - 1)]
    print_fight_menu()

def use_item():
    '''Use items to regain health and inflict damage to your opponent'''
    pass

def attack_enemy():
    print("You attacked " + player.current_room["enemy"]["name"] + " with your " + player.current_weapon["name"])
    print("You inflicted " + str(player.current_weapon["damage"]) + " damage!")
    player.current_room["enemy"]["health"] -= player.current_weapon["damage"]
    time.sleep(3)
    if player.current_room["enemy"]["health"] <= 0:
        print("You killed " + player.current_room["enemy"]["name"] + "!")
        time.sleep(2)
        return True
    print(player.current_room["enemy"]["name"] + " attacked you with " + player.current_room["enemy"]["weapon"]["name"])
    print("You lost " + str(player.current_room["enemy"]["weapon"]["damage"]) + " health!\n")
    player.health -= player.current_room["enemy"]["weapon"]["damage"]
    time.sleep(3)
    if player.health <= 0:
        print("You have been killed.")
        time.sleep(3)
        return False
    return True

def print_fight_stats():
    print("You Are Fighting " + player.current_room["enemy"]["name"])
    print("Their Health: " + str(player.current_room["enemy"]["health"]))
    print("Your Health: " + str(player.health))
    print("Your Weapon: " + player.current_weapon["name"])

def print_fight_menu():
    print_fight_stats()
    return int(input("\nPress 1 for Weapon Selection\nPress 2 to Use Item\nPress 3 to Attack Enemy\n"))

def fight_scene():
    alive = True
    while alive:
        choice = print_fight_menu()
        if choice == 1:
            weapon_selection()
        elif choice == 2:
            use_item()
        elif choice == 3:
            if attack_enemy():
                if player.current_room["enemy"]["health"] <= 0:
                    alive = False
            else:
                alive = False
