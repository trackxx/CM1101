import weapons

item_student_card = {
    "id": "student card",
    "name": "a Student Card",
    "description": """Your student card. Whoever took the picture, made sure to get your worse profile""",
    "interactable": False
}

item_wallet = {
    "id": "wallet",
    "name": "a Wallet",
    "description": """Your wallet. As empty as your ex's brain.""",
    "interactable": False
}

item_keys = {
    "id": "keys",
    "name": "Keys",
    "description": """Your keys. It's a huge relief to still have those.""",
    "interactable": False
}

item_phone = {
    "id": "phone",
    "name": "an iPhone",
    "description": """Your overpriced, not compatible with anything that isn't Apple phone with a cracked screen. Boy, get an Android phone.""",
    "interactable": False
}

item_wristband = {
    "id": "wristband",
    "name": "a VIP Wristband",
    "description": """'Look at me, I paid more money than you to enter the same club, but with a free shot' wristband""",
    "interactable": False
}

item_hotdog = {
    "id": "hotdog",
    "name": "a Hotdog",
    "description": """Student's breakfast, lunch, dinner and a nightime snack in one thing. God bless fast food.""",
    "interactable": True,
    "type": "health",
    "health": 20
}

item_money = {
    "id": "money",
    "name": "Money",
    "description": """If you need a description for money, you probably can't even read this.""",
    "interactable": False
}

item_number = {
    "id": "number",
    "name": "a Number",
    "description": """description""",
    "interactable": False
}

item_id = {
    "id": "id",
    "name": "an ID",
    "description": """description""",
    "interactable": False
}

item_cologne = {
    "id": "cologne",
    "name": "Cologne",
    "description": """A Cologne. You either use too much of it, and the whole bus hates you, or you don't use enough and smell wears off before you even leave your house.""",
    "interactable": True,
    "type": "attractive"
}

item_water = {
    "id": "water",
    "name": "Water",
    "description": """Blessed nectar of gods. Underrestimated during the night, praised the next day.""",
    "interactable": True,
    "type": "drunkness",
    "drunkness": -10
}

item_jager = {
    "id": "jager",
    "name": "a Jagerbomb",
    "description": """*Hick* Germans sure know *hick* how to make us get wasted.""",
    "interactable": True,
    "type": "drunkness",
    "drunkness": 20
}

item_vodka = {
    "id": "vodka",
    "name": "a Vodka Shot",
    "description": """IN SOVIET RUSSIA, VODKA DRINKS YOU.""",
    "interactable": True,
    "type": "drunkness",
    "drunkness": 30
}

item_ticket = {
    "id": "ticket",
    "name": "a Cloakroom Ticket",
    "description": """A regular cloakroom ticket. As your grandma said - 'Put your jacket on before you go outside.'""",
    "interactable": False
}

item_card = {
    "id": "card",
    "name": "a Taxi Card",
    "description": """Phone number of the only taxi corporation in the city, that doesn't rip you off.""",
    "interactable": False
}

item_jacket = {
    "id": "jacket",
    "name": "a Jacket",
    "description": """Your good, old jacket. Wait, what's that brown spot on the sleeve?""",
    "interactable": True,
    "type": "items",
    "items": [item_keys, item_card]
}

item_table = {
    "id": "table",
    "name": "a Table",
    "description": """A wooden table. There's something on it.""",
    "interactable": True,
    "type": "weapons",
    "items": [weapons.weapon_bottle, weapons.weapon_bucket]
}

item_hotdog_stand = {
    "id": "stand",
    "name": "a Hotdog Stand",
    "description": """You stomach plays the song of it's people. God, you'd kill for a hot dog.""",
    "interactable": True,
    "type": "weapons",
    "items": [weapons.weapon_spatula, weapons.weapon_hotdog]
}
