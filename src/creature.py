# defines base creature in the base. all monsters, Characters, npcs, and critters derive from this.
from collections import defaultdict
import sys
import os
import json

from src.bodypart import Bodypart


class Creature:
    def __init__(self):
        self.stats = defaultdict(dict)
        self.stats["strength"]["base"] = 8
        self.stats["strength"]["max"] = 20
        self.stats["dexterity"]["base"] = 8
        self.stats["dexterity"]["max"] = 20
        self.stats["intelligence"]["base"] = 8
        self.stats["intelligence"]["max"] = 20
        self.stats["perception"]["base"] = 8
        self.stats["perception"]["max"] = 20
        self.stats["constitution"]["base"] = 8
        self.stats["constitution"]["max"] = 20
        # known_recipes[0] = Recipe(ident, favorite) -  pull full recipe info from RecipeManager['ident'] - NPCs may know recipes that's why its in Creature
        self.known_recipes = list()
        # what each creature wants to do this turn and the upcoming turns. contains a list of Action(s) that are processed by the server.
        self.command_queue = list()
        self.gender = "male"
        
        # name is optional here. characters and most NPCs would have a name.
        self.name = None
        
        # what is this creature able to do?
        self.possible_actions = [
            "move",
            "attack",
            "sneak",
            "craft",
            "activate",
            "wear",
            "remove",
            "reload",
        ]

        # how much speed can this creature spend towards actions per turn?
        self.speed_per_turn = 100

        self.tile_ident = "starter_race"  # base ident for new creatures.
        self.move_mode = "walk"  # 'walk', 'run', 'sneak'

        # list of body parts this creature has. normal human has 2 arms, 2 hands, 2 legs, torso, head, and 2 feet. head and torso are both vital organs.
        # body_parts are where items get equipped.
        self.body_parts = [
            Bodypart("HEAD_0", True),
            Bodypart("TORSO_0", True),
            Bodypart("ARM_LEFT"),
            Bodypart("ARM_RIGHT"),
            Bodypart("LEG_LEFT"),
            Bodypart("LEG_RIGHT"),
            Bodypart("FOOT_LEFT"),
            Bodypart("FOOT_RIGHT"),
            Bodypart("HAND_LEFT"),
            Bodypart("HAND_RIGHT"),
        ]
        # the 'special' area where items held on the mouse cursor are stored.
        self.grabbed = None
