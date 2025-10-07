##############################################################################
# Title: Blastoise Dictionary
# Assignment: Pokemon Dictionary Project
# Class: CS 30
# Coder: Atticus
# Date: 9/18/2025
# Version: 1.0
##############################################################################
"""Blastoise pokemon dictionary."""
##############################################################################
# Imports and global variables------------------------------------------------
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
# Main------------------------------------------------------------------------
for trait in blastoise:
    value = blastoise.get(trait)
    if type(value) != list:
        # Print single value
        print(f"Blastoise's {trait}: {value}")
    elif type(value) == list:
        # Print multiple values
        print(f"Blastoise's {trait}: ")
        for item in value:
            print(f" - {item}")
    else:
        print("Invalid value type.")
