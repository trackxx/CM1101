import weapons

item_student_card = {
    "id": "student card",
    "name": "a Student Card",
    "description": """DECRIPTION""",
    "interactable": False
}

item_wallet = {
    "id": "wallet",
    "name": "a Wallet",
    "description": """DECRIPTION""",
    "interactable": False
}

item_keys = {
    "id": "keys",
    "name": "Keys",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_phone = {
    "id": "phone",
    "name": "an iPhone",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_wristband = {
    "id": "wristband",
    "name": "a VIP Wristband",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_hotdog = {
    "id": "hotdog",
    "name": "a Hotdog",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "health",
    "health": 20
}

item_money = {
    "id": "money",
    "name": "Money",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_number = {
    "id": "number",
    "name": "a Number",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_id = {
    "id": "id",
    "name": "an ID",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_cologne = {
    "id": "cologne",
    "name": "Cologne",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "attractive"
}

item_water = {
    "id": "water",
    "name": "Water",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "drunkness",
    "drunkness": -10
}

item_jager = {
    "id": "jager",
    "name": "a Jagerbomb",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "drunkness",
    "drunkness": 20
}

item_vodka = {
    "id": "vodka",
    "name": "a Vodka Shot",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "drunkness",
    "drunkness": 30
}

item_ticket = {
    "id": "ticket",
    "name": "a Cloakroom Ticket",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_card = {
    "id": "card",
    "name": "a Taxi Card",
    "decription": """DECRIPTION""",
    "interactable": False
}

item_jacket = {
    "id": "jacket",
    "name": "a Jacket",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "items",
    "items": [item_keys, item_card]
}

item_table = {
    "id": "table",
    "name": "a Table",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "weapons",
    "items": [weapons.weapon_bottle, weapons.weapon_bucket]
}

item_hotdog_stand = {
    "id": "stand",
    "name": "a Hotdog Stand",
    "decription": """DECRIPTION""",
    "interactable": True,
    "type": "weapons",
    "items": [weapons.weapon_spatula, weapons.weapon_hotdog]
}
