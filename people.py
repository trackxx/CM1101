import weapons
import items

person_toilet_guy = {
    "name": "Toilet Man",
    "health": 20,
    "dialog": ["No spray, no lay... No splash, no gash... No Armarni, no punani... You gotta wash your fingers for de mingers...",
               "No thanks..", "Here, have this..", "*Hands Washed*", "That'll be £3 please sir.", "I have no money...", "You owe me £3...", "*Pushed Over*"],
    "fight": True,
    "items": False,
    "alive": True,
    "weapon": weapons.weapon_lollipop
}

person_hotdog_guy = {
    "name": "Hotdog Guy",
    "dialog": ["£1.50 for a Hotdog?"],
    "fight": False,
    "items": True,
    "items": [items.item_hotdog],
    "requirements": [],
    "cost": 150
}

person_wallet = {
    "name": "Smoking Friend",
    "health": 25,
    "dialog": ["Hey! I found you're wallet outside."],
    "fight": True,
    "items": False,
    "weapon": weapons.weapon_lighter
}

person_cloakroom = {
    "name": "Cloakroom Guy",
    "dialog": ["Would you like to retrieve your items?"],
    "fight": False,
    "items": True,
    "items": [items.item_jacket],
    "requirements": [items.item_ticket],
    "cost": 0
}

person_housemate_girl = {
    "name": "Housemate Girl",
    "dialog": ["Why would you do that?", "I'm sorry?"],
    "fight": False,
    "items": False
}

person_housemate_guy = {
    "name": "Housemate Guy",
    "health": 30,
    "dialog": ["Just leave.", "But I've lost everything..", "Haha good, now get lost.", "What..."],
    "fight": True,
    "items": False,
    "weapon": weapons.weapon_fists
}

person_coursemate_girl = {
    "name": "Coursemate Girl",
    "dialog": ["Hey @", "Hey, can I buy you a drink?"],
    "fight": False,
    "items": False
}

person_coursemate_boyfriend = {
    "name": "Coursemate Girl's Boyfriend",
    "health": 35,
    "dialog": ["Oi", "...", "That's my girlfriend you mug"],
    "fight": True,
    "items": False,
    "weapon": weapons.weapon_cup
}

person_barman_one = {
    "name": "Barman",
    "dialog": ["Would you like a drink of water?"],
    "fight": False,
    "items": True,
    "items": [items.item_water],
    "requirements": [],
    "cost": 0
}

person_barman_two = {
    "name": "Barman",
    "dialog": ["Would you like a jagerbomb, two for £1.50?"],
    "fight": False,
    "items": True,
    "items": [items.item_jager],
    "requirements": [],
    "cost": 150
}

person_smoking_area_guy = {
    "name": "Smoking Area Guy",
    "dialog": ["Mate I gotta bounce, do you want my VIP wristband?"],
    "fight": False,
    "items": True,
    "items": [items.item_wristband],
    "requirements": [],
    "cost": 0
}

person_rugby_guy = {
    "name": "Rugby Guy",
    "health": 40,
    "weapon": weapons.weapon_big_fists
}

person_hot_girl = {
    "name": "Hot Girl",
    "dialog": ["Hey, what's your name?", "@", "You're cute, have these shots with me", "*Vodka Shot*", "I have to go, I've lost my friends but it's nice to meet you, @. Call me."],
    "fight": False,
    "items": True,
    "items": [items.item_vodka, items.item_number],
    "requirements": [items.item_cologne, items.item_phone],
    "cost": 0
}

person_bouncer = {
    "name": "Bouncer",
    "health": 50,
    "weapon": weapons.weapon_giant_fists
}
