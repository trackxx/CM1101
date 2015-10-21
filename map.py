from items import *
from people import *

room_entrance = {
    "name": "Entrance",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Exit", "east": "Rnb Room", "north": "Stairs to first floor"},

    "items": [],

    "people": [person_bouncer]
}

room_rnb_bar = {
    "name": " Rnb Bar",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Rnb Room"},

    "items": [],

    "people": []
}

room_Rnb = {
    "name": "Rnb Room",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Entrance", "east": "Rnb Bar"},

    "items": [item_phone],

    "people": []
}

room_cloak = {
    "name": "Cloak room",

    "description": "< DESCRIPTION HERE >",

    "exits": {"east": "Stairs to first floor"},

    "items": [],

    "people": [person_cloakroom]
}

room_stairs1 = {
    "name": "Stairs to first floor",

    "description": "< DESCRIPTION HERE >",

    "exits": {"north": "Stairs to second floor", "south": "Entrance", "east": "Hotdog stand"},

    "items": [],

    "people": []
}

room_hotdog = {
    "name": "Hotdog stand",

    "description": "< DESCRIPTION HERE >",

    "exits": {"east": "Toilet", "west": "Stairs to first floor"},

    "items": [item_wallet, item_hotdog_stand],

    "people": [person_hotdog_guy, person_wallet]
}

room_toilet1 = {
    "name": "Toilet",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Hotdog stand"},

    "items": [item_money],

    "people": [person_toilet_man]
}

room_toilet2 = {
    "name": "Toilet2",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Hotdog stand"},

    "items": [item_cologne],

    "people": []
}

room_stairs2 = {
    "name": "Stairs to second floor ",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Vip Room", "south": "Stairs to first floor", "east": "Pryzm Room", "north": "Stairs to third floor"},

    "items": [],

    "people": []
}

room_stairs3 = {
    "name": "Stairs to third floor ",

    "description": "< DESCRIPTION HERE >",

    "exits": {"north": "Disco Room", "south": "Stairs to second floor"},

    "items": [],

    "people": []
}

room_vip = {
    "name": "Vip Room",

    "description": "< DESCRIPTION HERE >",

    "exits": {"east": "Stairs to second floor"},

    "items": [item_student_card, item_table],

    "people": [person_housemate_girl, person_housemate_guy]
}

room_Main = {
    "name": "Pryzm Room",

    "description": "< DESCRIPTION HERE >",

    "exits": {"east": "Pryzm room Bar", "west": "Stairs to second floor"},

    "items": [],

    "people": []
}

room_main_bar = {
    "name": "Pryzm room Bar",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Pryzm Room", "south": "Smoking area"},

    "items": [item_id],

    "people": [person_coursemate_girl, person_coursemate_boyfriend, person_barman_one]
}

room_smoking = {
    "name": "Smoking area",

    "description": "< DESCRIPTION HERE >",

    "exits": {"north": "Pryzm room bar"},

    "items": [item_wristband],

    "people": [person_smoking_area_guy]
}

room_disco = {
    "name": "Disco Room",

    "description": "< DESCRIPTION HERE >",

    "exits": {"east": "Disco room bar", "south": "Stairs to second floor"},

    "items": [item_number, item_ticket],

    "people": [person_rugby_guy]
}

room_disco_bar = {
    "name": "Disco room bar",

    "description": "< DESCRIPTION HERE >",

    "exits": {"west": "Disco Room"},

    "items": [item_vodka],

    "people": [person_hot_girl, person_barman_two]
}

room_exit = {
    "name": "exit",

    "description": "< DESCRIPTION HERE >",

    "exits": {},

    "items": [],

    "people": []
}

rooms = {
    "Entrance": room_entrance,
    "Rnb Bar": room_rnb_bar,
    "Rnb Room": room_Rnb,
    "Cloak room": room_cloak,
    "Stairs to first floor": room_stairs1,
    "Hotdog stand": room_hotdog,
    "Toilet": room_toilet1,
    "Toilet2": room_toilet2,
    "Stairs to second floor": room_stairs2,
    "Vip Room": room_vip,
    "Pryzm Room": room_Main,
    "Pryzm room Bar": room_main_bar,
    "Smoking area": room_smoking,
    "Disco Room": room_disco,
    "Disco room bar": room_disco_bar,
    "Exit": room_exit,
    "Stairs to third floor": room_stairs3,
}
