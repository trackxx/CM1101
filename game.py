import os
import player
import time
from fight import *
from menu import *
from items import *
from normalise import *
from map import rooms

def list_of_items(items):
    item_list = ""
    for item in items:
        item_list += item["name"] + ", "
    item_list = item_list[:-2]
    return item_list


def print_room_items(room):
    items = room["items"]
    item_list = list_of_items(items)
    room_items = "There is "
    if(len(item_list) > 0):
        room_items += item_list
        room_items += " here.\n"
        print(room_items)


def print_inventory_items(items):
    item_list = list_of_items(items)
    room_items = "You have "
    if(len(item_list) > 0):
        room_items += item_list
        room_items += ".\n"
        print(room_items)


def print_room(room):
    # Display room name
    print("\n" + room["name"].upper() + "\n")
    # Display room description
    print(room["description"] + "\n")
    # Display room items
    print_room_items(room)

def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_stats():
    print("Stats:")
    print("Health: " + str(player.health))
    print("Drunk: " + str(player.drunk))
    print("Money: £" + str((player.money / 100)) + "\n")

def print_menu(exits, room_items, inv_items, people):
    untalkable = ["Coursemate Girl's Boyfriend", "Smoking Friend", "Toilet Man"]
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        if(item["storable"]):
            print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
        if(item["interactable"]):
            print("INTERACT " + item["id"].upper() + " to interact with " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ".")
        if item["interactable"]:
            print("INTERACT " + item["id"].upper() + " to interact with " + item["name"] + ".")
    for person in people:
        if not person["name"] in untalkable:
            print("TALK " + person["name"].upper() + " to talk to " + person["name"] + ".")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    directions = ["north", "east", "south", "west"]
    if direction.lower() in directions:
        can_move = True
        for item in rooms[player.current_room["exits"][direction]]["requirements"]:
            if item not in player.inventory:
                can_move = False
        if(can_move):
            player.current_room = rooms[player.current_room["exits"][direction]]
        else:
            print("You can't go here.")
            time.slee(2)


def execute_take(item_id):
    taken = False
    for item in player.current_room["items"]:
        if(item["id"] == item_id):
            player.current_room["items"].remove(item)
            player.inventory.append(item)
            taken = True

    if not taken:
        print("You cannot take that.")
        time.sleep(1)


def execute_drop(item_id):
    dropped = False
    for item in player.inventory:
        if(item["id"] == item_id):
            player.inventory.remove(item)
            player.current_room["items"].append(item)
            dropped = True

    if not dropped:
        print("You cannot take that.")

def execute_talk(person_name):
    str_person_name = person_name[0].capitalize()
    for word in person_name[1:]:
        str_person_name = str_person_name + " " + word.capitalize()
    try:
        for line in people[str_person_name]["dialog"]:
            print(line)
            time.sleep(2)
            if line.endswith("?"):
                if people[str_person_name]["items"] == []:
                    print("You have everthing you need from " + str_person_name + ".")
                    time.sleep(2)
                    break
                loop_counter = 0
                for response in people[str_person_name]["responses"]:
                    loop_counter += 1
                    print("Press", loop_counter, "to say: '" + response + "'")
                choice = input("Your choice: ")
                cost = int(people[str_person_name]["items"][0]["amount"])
                name = str(people[str_person_name]["items"][0]["name"])
                if int(choice) == 1:
                    if cost <= player.money:
                        player.inventory.extend(people[str_person_name]["items"][:])
                        people[str_person_name]["items"].clear()
                        print("You got " + name)
                        time.sleep(2)
                    else:
                        print("Can't afford it.")
                        time.sleep(2)
                elif int(choice) == 2:
                    print("You leave.")
                else:
                    print("That doesn't make sense.")
        time.sleep(2)
        if str_person_name == "Coursemate Girl":
            str_person_name = "Coursemate Girl's Boyfriend"
        if people[str_person_name]["fight"] == True:
            fight_scene(people[str_person_name])
    except KeyError:
        print("You cannot talk to " + str_person_name + ".")

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


def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1:])
        else:
            print("Talk to who?")

    elif command[0] == "interact":
        if len(command) > 1:
            execute_interact(command[1])
        else:
            print("Interact with what?")

    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items, people):
    # Display menu
    print_menu(exits, room_items, inv_items, people)
    # Read player's input
    user_input = input("> ")
    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]

def check_completion():
    if player.current_room["name"] == "exit":
        return True
    else:
        return False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    player.start_time = int(time.time())
    while not check_completion():
        # Display game status (room description, inventory etc.)
        print_room(player.current_room)
        print_stats()
        print_inventory_items(player.inventory)
        for person in player.current_room["people"]:
            if person["fight"] == True and person["alive"] == True and person["health"] > 0:
                execute_talk(person["name"].split(" "))
        if player.health <= 0:
            return False
        # Show the menu with possible actions and ask the player
        command = menu(player.current_room["exits"], player.current_room["items"], player.inventory, player.current_room["people"])
        # Execute the player's command
        execute_command(command)
        clear_console()
    player.end_time = int(time.time())
    return True

# This is the entry point of our program
def main():
    print("-----------------------------------------------------------------------")
    print("__          ________ _      _____ ____  __  __ ______   _______ ____   ")
    print("\ \        / /  ____| |    / ____/ __ \|  \/  |  ____| |__   __/ __ \  ")
    print(" \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__       | | | |  | | ")
    print("  \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|      | | | |  | | ")
    print("   \  /\  /  | |____| |___| |___| |__| | |  | | |____     | | | |__| | ")
    print("    \/  \/   |______|______\_____\____/|_|  |_|______|    |_|  \____/  ")
    print("                                                                       ")
    print("                                                                       ")
    print(" _____  _______     __________  __   ____  _____  ______          _  __")
    print("|  __ \|  __ \ \   / /___  /  \/  | |  _ \|  __ \|  ____|   /\   | |/ /")
    print("| |__) | |__) \ \_/ /   / /| \  / | | |_) | |__) | |__     /  \  | ' / ")
    print("|  ___/|  _  / \   /   / / | |\/| | |  _ <|  _  /|  __|   / /\ \ |  <  ")
    print("| |    | | \ \  | |   / /__| |  | | | |_) | | \ \| |____ / ____ \| . \ ")
    print("""|_|    |_|  \_\ |_|  /_____|_|  |_| |____/|_|  \_\______/_/    \_\_|\_\\
    """)
    print("")
    print("-----------------------------------------------------------------------")
    print("")
    show_menu()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
