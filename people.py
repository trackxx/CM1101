import weapons
import items
import player

person_toilet_man = {
    "name": "Toilet Man",
    "health": 20,
    "dialog": ["TOILET MAN: No spray, no lay... No splash, no gash... No Armarni, no punani... You gotta wash your fingers for de mingers...",
               "YOU: No thanks..", "TOILET MAN: Here, have this..", "*Hands Washed*", "TOILET MAN: That'll be £3 please sir.", "YOU: I have no money...", "TOILET MAN: You owe me £3...", "*Pushed Over*"],
    "fight": True,
    "items": False,
    "alive": True,
    "weapon": weapons.weapon_lollipop
}

person_hotdog_guy = {
    "name": "Hotdog Guy",
    "dialog": ["HOTDOG GUY: £1.50 for a Hotdog?"],
    "responses": ["Yeah, go on.", "No thanks."],
    "fight": False,
    "items": True,
    "items": [items.item_hotdog],
    "requirements": [],
    "cost": 150
}

person_wallet = {
    "name": "Smoking Friend",
    "health": 25,
    "dialog": ["SMOKING FRIEND: Hey! I found you're wallet outside.", "You check your wallet and it's completely empty.", "YOU: Where's my money?", "SMOKING FRIEND: I don't know"],
    "fight": True,
    "items": False,
    "weapon": weapons.weapon_lighter
}

person_cloakroom = {
    "name": "Cloakroom Guy",
    "dialog": ["CLOAKROOM GUY: Would you like to retrieve your items?"],
    "fight": False,
    "items": True,
    "items": [items.item_jacket],
    "requirements": [items.item_ticket],
    "cost": 0
}

person_housemate_girl = {
    "name": "Housemate Girl",
    "dialog": ["HOUSEMATE GIRL: Why would you do that?", "YOU: I'm sorry?"],
    "fight": False,
    "items": False
}

person_housemate_guy = {
    "name": "Housemate Guy",
    "health": 30,
    "dialog": ["HOUSEMATE GUY: Just leave.", "YOU: But I've lost everything..", "HOUSEMATE GUY: Haha good, now get lost.", "YOU: What..."],
    "fight": True,
    "items": False,
    "weapon": weapons.weapon_fists
}

person_coursemate_girl = {
    "name": "Coursemate Girl",
    "dialog": ["COURSEMATE GIRL: Hey!", "YOU: Hey, can I buy you a drink?"],
    "fight": False,
    "items": False
}

person_coursemate_boyfriend = {
    "name": "Coursemate Girl's Boyfriend",
    "health": 35,
    "dialog": ["COURSEMATE GIRL'S BOYFRIEND: Oi", "YOU: ...", "COURSEMATE GIRL'S BOYFRIEND: That's my girlfriend you mug"],
    "fight": True,
    "items": False,
    "weapon": weapons.weapon_cup
}

person_barman_one = {
    "name": "Barman",
    "dialog": ["BARMAN: Would you like a drink of water?"],
    "fight": False,
    "items": True,
    "items": [items.item_water],
    "requirements": [],
    "cost": 0
}

person_barman_two = {
    "name": "Disco Room Barman",
    "dialog": ["DISCO ROOM BARMAN: Would you like a jagerbomb, two for £1.50?"],
    "fight": False,
    "items": True,
    "items": [items.item_jager],
    "requirements": [],
    "cost": 150
}

person_smoking_area_guy = {
    "name": "Smoking Area Guy",
    "dialog": ["SMOKING AREA GUY: Mate I gotta bounce, do you want my VIP wristband?"],
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
    "dialog": ["HOT GIRL: Hey, what's your name?", "YOU: Do this shit in a bit", "HOT GIRL: You're cute, have these shots with me", "*Vodka Shot*", "HOT GIRL: I have to go, I've lost my friends but it was nice meeting you. Call me."],
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

people = {
    "Toilet Man": person_toilet_man,
    "Hotdog Guy": person_hotdog_guy,
    "Smoking Friend": person_wallet,
    "Cloakroom Guy": person_cloakroom,
    "Housemate Girl": person_housemate_girl,
    "Housemate Guy": person_housemate_guy,
    "Coursemate Girl": person_coursemate_girl,
    "Coursemate Girl's Boyfriend": person_coursemate_boyfriend,
    "Barman": person_barman_one,
    "Disco Room Barman": person_barman_two,
    "Smoking Area Guy": person_smoking_area_guy,
    "Rugby Guy": person_rugby_guy,
    "Hot Girl": person_hot_girl,
    "Bouncer": person_bouncer
}
