##############################################################################
# Title: Pokemon Database
# Assignment: Pokemon Database Project
# Class: CS 30
# Coder: Atticus
# Contributors: Brody, James, Leo
# Date: 9/18/2025
# Version: 1.0
##############################################################################
"""Populate a database of Pokemon."""
##############################################################################
# Imports and global variables -----------------------------------------------
blastoise = {"pokedex": """Blastoise is a large, bipedal, reptilian Pokémon.
                           It has a blue body with small purple eyes, a
                           light brown belly, and a stubby tail. It has a
                           large brown shell with two powerful water
                           cannons on either side, which can be withdrawn""",
             "type": ["water"],
             "evolution": 3,
             "hp": 79,
             "atk": 83,
             "def": 100,
             "moves": ["torrent", "rain dish"],
}

blaziken = {"pokedex": """When facing a tough foe, it looses flames from its
                          wrists. Its powerful legs let it jump clear over
                          buildings.""",
            "type": ["fighting", "fire"],
            "evolution": 3,
            "hp": 80,
            "atk": 120,
            "def": 70,
            "moves": ["swords dance", "flare blitz", "low kick",
                      "stone edge"],
}

jigglypuff = {"pokedex": """Jigglypuff, known as the Balloon Pokémon,"
                            is a Normal/Fairy-type Pokémon introduced
                            in Generation I. It is recognized for its
                            ability to lull opponents to sleep by
                            singing a soothing melody.""",
              "type": ["normal", "fairy"],
              "evolution": 1,
              "hp": 115,
              "atk": 40,
              "def": 25,
              "moves": ["sing", "defence curl", "pound"],
}

froakie = {"pokedex": """Small blue frog Pokemon. Evolves into "Frogadier.""",
           "type": ["water"],
           "evolution": 1,
           "hp": 41,
           "atk": 56,
           "def": 40,
           "moves": ["pound", "growl", "water gun", "quick attack"],
}

pokemon = {"blastoise": blastoise,
           "blaziken": blaziken,
           "froakie": froakie,
           "jigglypuff": jigglypuff
}
# Main------------------------------------------------------------------------
# Printing four sentences
print(f"Jigglypuff's evolution is {pokemon['jigglypuff']['evolution']}")
print(f"Froakie's attack power is {pokemon['froakie']['atk']}")
print(f"Blastoise is described as:\"{pokemon['blastoise']['pokedex']}\"")
print(f"Blakizen's hp is {pokemon['blaziken']['hp']}")
# Printing all abilities
print("\nThe abilities of all the pokemon are:")
move_counter = 1
for creature in pokemon.values():
    for move in creature["moves"]:
        print(f" {move_counter}  {move.title()}")
        move_counter += 1
