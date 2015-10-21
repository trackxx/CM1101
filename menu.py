import hashlib
import json
import player
from normalise import *
from game import *
import map

def md5_hash(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()

def add_leaderboards(name, time):
    f = open("leaderboards", 'r+')
    leaderboard = ""
    added = False
    for line in f:
        details = line.split(",")
        leaderboard_time = int(details[1].rstrip('\n'))
        if(time <= leaderboard_time):
            if not added:
                leaderboard += name + "," + str(time) + "\n"
                added = True
        leaderboard += line
    f.close()
    if leaderboard == "":
        leaderboard = name + "," + str(time) + "\n"
    f = open("leaderboards", 'w')
    f.write(leaderboard)
    f.close()

def leaderboards():
    print("\nLeaderboards:")
    f = open("leaderboards", 'r+')
    position = 1
    for line in f:
        details = line.split(",")
        print(str(position) + ". " + details[0] + " (" + details[1].rstrip('\n') + ")")
        position += 1
    f.close()

def new_game():
    player.name = input("What is your name? ")
    if play_game():
        print("Congratulations you escaped from PRYZM!")
        completion_time = player.end_time - player.start_time
        add_leaderboards(player.name, completion_time)
        leaderboards()
    else:
        print("GAME OVER")


def save_game():
    save_name = input("\nPlease enter a name for your save: ")
    print("Saving Game...")
    game_stats = {}
    room_stats = map.rooms
    game_stats["rooms"] = room_stats
    game_stats["inventory"] = player.inventory
    game_stats["active_weapons"] = player.active_weapons
    game_stats["current_weapon"] = player.current_weapon
    game_stats["current_room"] = player.current_room
    game_stats["health"] = player.health
    game_stats["drunk"] = player.drunk
    game_stats["money"] = player.money
    game_stats["name"] = player.name
    game_stats["start_time"] = player.start_time

    game_hash = md5_hash(str(player.start_time) + player.name + save_name)
    game_stats["hash"] = game_hash
    f = open(save_name, 'w')
    f.write(json.dumps(game_stats))
    print("Game saved successfully!")
    f.close()

def load_game():
    save_name = input("\nPlease enter the name of your game save: ")
    print("Loading Game...")
    f = open(save_name, 'r')
    game_stats = json.loads(f.read())
    f.close()
    save_hash = game_stats["hash"]
    hash_check = md5_hash(str(game_stats["start_time"]) + game_stats["name"] + save_name)
    if(hash_check != save_hash):
        print("Save file is invalid")
    else:
        map.rooms = game_stats["rooms"]
        player.inventory = game_stats["inventory"]
        player.active_weapons = game_stats["active_weapons"]
        player.current_weapon = game_stats["current_weapon"]
        player.current_room = game_stats["current_room"]
        player.health = game_stats["health"]
        player.drunk = game_stats["drunk"]
        player.money = game_stats["money"]
        player.name = game_stats["name"]
        player.start_time = game_stats["start_time"]
        print("Game loaded successfully")
        start_game()

def show_menu():
    menu_items = ["New Game", "Save Current Game", "Load Game", "Leaderboards"]
    for i in range(0, len(menu_items)):
        print("Press " + str(i + 1) + " for " + menu_items[i])
    selection = str(input("What would you like to do? "))
    if selection == "1":
        new_game()
    elif selection == "2":
        save_game()
    elif selection == "3":
        load_game()
    elif selection == "4":
        leaderboards()
