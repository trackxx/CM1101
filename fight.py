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

def consume_item(item):
        if item["type"] == "money":
            player.money += int(item["amount"])
            print("You found £" + str(player.money / 100) + "!")
        elif item["type"] == "drunkness":
            player.drunk += int(item["amount"])
            print("You drank " + item["name"])
        elif item["type"] == "health":
            player.health += int(item["amount"])
            print("You had a " + item["name"])
        elif item["type"] == "weapons":
            for i in range(0, len(item["items"])):
                print("Press " + str(i + 1) + " For " + item["items"][i]["name"])
            choice = int(input("Please choose a weapon: "))
            player.active_weapons.append(item["items"][(choice - 1)])
            print("You picked up " + item["items"][(choice - 1)]["name"])
        elif item["type"] == "item":
            for i in range(0, len(item["items"])):
                player.inventory.append(item["items"])
                print("You found " + item["name"])

def execute_interact(item_id):
    for item in player.current_room["items"]:
        if(item["id"] == item_id):
            consume_item(item)
            player.current_room["items"].remove(item)
            time.sleep(2)
    for item in player.inventory:
        if(item["id"] == item_id):
            consume_item(item)
            player.inventory.remove(item)
            time.sleep(2)

def use_item():
    '''Use items to regain health and inflict damage to your opponent'''
    for item in player.inventory:
        if item["interactable"] == True:
            choice = input("INTERACT " + item["id"].upper() + " to interact with " + item["name"] + ".")
            normalised_user_input = normalise_input(choice)
            execute_interact(normalised_user_input[1])

def attack_enemy(index):
    print("You attacked " + index["name"] + " with your " + player.current_weapon["name"])
    print("You inflicted " + str(player.current_weapon["damage"]) + " damage!")
    index["health"] -= player.current_weapon["damage"]
    time.sleep(3)
    if index["health"] <= 0:
        print("You killed " + index["name"] + "!\n")
        time.sleep(2)
        return True
    print(index["name"] + " attacked you with " + index["weapon"]["name"])
    print("You lost " + str(index["weapon"]["damage"]) + " health!")
    player.health -= index["weapon"]["damage"]
    time.sleep(3)
    if player.health <= 0:
        print("You have been killed.\n")
        time.sleep(3)
        return False
    return True

def print_fight_stats(index):
    print("\nYou Are Fighting " + index["name"])
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
                    index["alive"] = False
                    alive = False
            else:
                alive = False
