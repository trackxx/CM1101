from items import *

room_factory = {
    "name": "Factory Floor",

    "description":
    """You are standing in the middle of the cheese factory floor. You see a cheese grater 
    and a block of cheese """,

    "exits": {"south": "Staff Room", "east": "Locker room", "west": "Parking"},

    "items": [item_cheese_grater,item_cheese]
}

room_staff = {
    "name": "Staff Room",

    "description":
    """This room is where you spent many lunch breaks opening 
    up the fridge to find someone has already eatten your sandwitches and replaces
    it with a sticker""",

    "exits": {"north": "Factory Floor"},

    "items": [item_sticker,item_id]
}

room_locker = {
    "name": "Locker room",

    "description":
    """A room packed with lockers. to your surprise there is a note on your locker 
    """,

    "exits": {"west": "Factory Floor"},

    "items": [item_wallet,item_mobile,item_note ]
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in a car park remembering that you dont actually own a car
    a scooter to work every day. Your scooter is up against the wall.""",

    "exits": {"east": "Office", "south": "Factory Floor"},

    "items": [item_scooter]
}

room_office = {
    "name": "Managers Office",

    "description":
    """In this room lives the guy who has made your life a living hell for the past 10 years.""",

    "exits": {"west": "Parking"},

    "items": []
}

rooms = {
    "Factory Floor": room_factory,
    "Staff Room": room_staff,
    "Locker room": room_locker,
    "Parking": room_parking,
    "Office": room_office
}

