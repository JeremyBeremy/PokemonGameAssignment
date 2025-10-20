##############################################################################
# Title: Pokemon Menu System
# Assignment: Pokemon (part 3)
# Class: CS 30
# Coder: Atticus
# Date: 10/06/2025
# Version: 3.2
##############################################################################
"""A pokemon-style menu system for creating a pokemon.
The user can choose their own name, the species of their pokemon, the name
of their pokemon, and the starter move that their pokemon will have. Once
the user has specified all of this information, they may begin the game.
"""
##############################################################################
# Imports and global variables -----------------------------------------------
playing = True
player = {"name": None, "active": None}
owned_pokemon = {}
starter_pokemon = {"species": None, "moves": [], "hp": 0.0}
starter_nickname = None

# Available pokemon
blastoise = {"desc": """Blastoise is a large, bipedal, reptilian Pokémon.
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

blaziken = {"desc": """When facing a tough foe, it looses flames from its
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

jigglypuff = {"desc": """Jigglypuff, known as the Balloon Pokémon,"
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

froakie = {"desc": """Small blue frog Pokemon. Evolves into "Frogadier.""",
           "type": ["water"],
           "evolution": 1,
           "hp": 41,
           "atk": 56,
           "def": 40,
           "moves": ["pound", "growl", "water gun", "quick attack"],
}

pokedex = {"blastoise": blastoise,
           "blaziken": blaziken,
           "froakie": froakie,
           "jigglypuff": jigglypuff
}


# Functions ------------------------------------------------------------------
def menu(text, actions, include_back=True):
    """Show a general-purpose menu and let the user pick an option.

    Parameters:
        text (str): menu text to show to user
        actions (dict_keys): things the user can do
        include_back (bool): enables returning to previous menu as option

    Returns:
        str: the user's choice
    """
    ordered_actions = list(actions)  # Convert to list
    ordered_actions.extend([glob_act for glob_act in global_actions])
    ordered_actions.remove("Back") if not include_back else ordered_actions
    while True:
        print("\n" + text)
        for index, action in enumerate(ordered_actions):
            print(f"[{index + 1}]  {action.capitalize()}")
        choice_num = force_input_dtype("Choice: ", "int")
        if 1 <= choice_num <= len(ordered_actions):
            return ordered_actions[choice_num - 1]
        else:
            print("Not a valid option!")


def force_input_dtype(msg, dtype):
    """Force the user's input to match a chosen data type.

    Parameters:
        msg (str): text prompt for user
        dtype (str): desired data type for user input

    Returns:
        choice (int/float/str): user input as desired dtype
    """
    dtypes = {"int": int, "float": float, "str": str}
    while True:
        try:
            choice = input(msg)
            return dtypes[dtype](choice)
        except ValueError:
            print(f"\nInvalid. Ensure your input is of type: {dtype}")


def game_intro():
    """Show intro backstory."""
    print("THIS IS THE GAME INTRO. INSERT EPIC BACKSTORY HERE.")


def pick_player_name():
    """Let the user pick their name."""
    player["name"] = input("\nPick your name: ")


def pick_pokemon_nickname():
    """Let the user name their pokemon."""
    global starter_nickname
    starter_nickname = input("\nGive your creature a name: ")


def start_menu():
    """Show the user start menu options."""
    action = menu("\nPick something to do", start_menu_actions.keys(),
                  include_back=False)
    if action in global_actions.keys():
        # Handle global actions
        global_actions[action]()
    else:
        # Perform start menu action
        start_menu_actions[action]()


def pick_character():
    """Pick a pokemon species."""
    poke_choice = menu("\nHere is a list of all available pokemon:",
                       pokedex.keys())
    # Handle global actions
    if poke_choice in global_actions:
        global_actions[poke_choice]()
    else:
        # Check if move is compatible with species
        owned_moves = starter_pokemon["moves"]
        try:
            if owned_moves[0] not in pokedex[poke_choice]["moves"]:
                starter_pokemon["moves"] = []
                print("You move you had chosen is not compatible with "
                      "the current pokemon. Please select another move.")
        except IndexError:
            pass
        starter_pokemon["species"] = poke_choice
        starter_pokemon["hp"] = pokedex[poke_choice]["hp"]
        print(f"You chose {poke_choice}")


def pick_move():
    """Choose a move for your pokemon from the moves of its species."""
    if starter_pokemon["species"]:
        available_moves = pokedex[starter_pokemon["species"]]["moves"]
        move_choice = menu("\nPick a move:", available_moves)
        if move_choice in global_actions:
            # Handle global actions
            global_actions[move_choice]()
        else:
            # Check if move is compatible with species
            starter_pokemon["moves"] = [move_choice]
    else:
        print("Please select a pokemon species first!")


def start_game():
    """Check if player is ready and begin the game."""
    global playing
    ready = True
    if not starter_pokemon["species"]:
        print("Your pokemon is missing a species!")
        ready = False
    if not starter_pokemon["moves"]:
        print("Your pokemon is missing a move!")
        ready = False
    if not starter_nickname:
        print("Your pokemon is missing a name!")
        ready = False
    if ready:
        owned_pokemon[starter_nickname] = starter_pokemon
        player["active"] = starter_nickname
        print(owned_pokemon)
        print(player)
        print("\n\n---------------------------------------------------------")
        print(f'Your first pokemon is named {starter_nickname}, and it is '
              f'a {owned_pokemon[starter_nickname]["species"].title()}.')
        print("Its moves are:")
        for move in starter_pokemon["moves"]:
            print(f" - {move.title()}")
        print("\nThe adventure begins... another time haha the game doesn't "
              "actually exist yet.")
        playing = False


def back():
    """Return to start menu."""
    pass


def quit_game():
    """Quit the game."""
    global playing
    playing = False
    print("\nQuit")


# Main -----------------------------------------------------------------------
# Define actions
start_menu_actions = {"Pick pokemon": pick_character,
                      "Pick move": pick_move,
                      "Pick nickname": pick_pokemon_nickname,
                      "Start game": start_game,
}
global_actions = {"Back": back,
                  "Quit": quit_game,
}
game_intro()
pick_player_name()
# Game loop
while playing:
    start_menu()
