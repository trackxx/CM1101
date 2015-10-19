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


def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ".")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    player.current_room = rooms[player.current_room["exits"][direction]]


def execute_take(item_id):
    taken = False
    for item in player.current_room["items"]:
        if(item["id"] == item_id):
            player.current_room["items"].remove(item)
            player.inventory.append(item)
            taken = True

    if not taken:
        print("You cannot take that.")


def execute_drop(item_id):
    dropped = False
    for item in player.inventory:
        if(item["id"] == item_id):
            player.inventory.remove(item)
            player.current_room["items"].append(item)
            dropped = True

    if not dropped:
        print("You cannot take that.")


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

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)
    # Read player's input
    user_input = input("> ")
    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]

def check_completion():
    if len(player.inventory) == 100:
        print("You have completed the game!")
        return True
    else:
        return False

def play_game():
    player.start_time = int(time.time())
    while not check_completion():
        # Display game status (room description, inventory etc.)
        print_room(player.current_room)
        print_inventory_items(player.inventory)
        # Show the menu with possible actions and ask the player
        command = menu(player.current_room["exits"], player.current_room["items"], player.inventory)
        # Execute the player's command
        execute_command(command)
        # fight_scene()
        if player.health <= 0:
            return False
    player.end_time = int(time.time())
    return True

# This is the entry point of our program
def main():
    print("Welcome to PRZYM BREAK\n")
    show_menu()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
