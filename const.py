# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Filename:    const.py
# Created:     03/16/2017
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------

""" Constants """
from random import choices

from sdl2 import SDL_Color


class WindowSize:
    """ Window width and height """

    WIDTH = 1024
    HEIGHT = 768


class Colors:
    """ Map colors"""

    WHITE = SDL_Color(255, 255, 255)
    BLACK = SDL_Color(0, 0, 0)

    RED = SDL_Color(255, 0, 0)
    GREEN = SDL_Color(0, 255, 0)
    BLUE = SDL_Color(0, 0, 255)


class HorseNames:
    """ Horse Names """
    NAMES = {"2nd Hand Sock": 0,
             "Accept the Length": 0,
             "Air Biscuit": 0,
             "Arthur or Martha": 0,
             "Axe Wound": 0,
             "Backdoor Bandit": 0,
             "Bankrupt Rage": 0,
             "Barkers Eggs": 0,
             "Barnton Bellbanger": 0,
             "Beanflicker": 0,
             "Beef Bandito": 0,
             "Biffin's Bridge": 0,
             "Billy Sastard": 0,
             "Bishop Basher": 0,
             "Bloated Bag": 0,
             "Bolt Shooter": 0,
             "Bronson": 0,
             "Bronx Cheer": 0,
             "Brown Eyed Girl": 0,
             "Buckmelad": 0,
             "Bush Bandit": 0,
             "Camel's Toe": 0,
             "Cauliflower Arse": 0,
             "Cheesy Chode": 0,
             "Cheesy Hornblower": 0,
             "Chocolate Channel": 0,
             "Chocolate Starfish": 0,
             "Chunder Munchkin": 0,
             "Chutney Bunker": 0,
             "Clown's Pocket": 0,
             "Cock Soup": 0,
             "Cocoa Shunter": 0,
             "Collar & Cuffs": 0,
             "Crack Horse": 0,
             "Cryptochid": 0,
             "Cunning Lingus": 0,
             "Dead Lemon": 0,
             "Dead Wipe": 0,
             "Diddy Ride": 0,
             "Dildonut & Burdock": 0,
             "Dong Johnson": 0,
             "Dr.Boogie": 0,
             "Duck My Sick": 0,
             "Dundee Ned": 0,
             "Facial Lancer": 0,
             "Fairy Hammock": 0,
             "Falkirk Boy": 0,
             "Filshie's Filly": 0,
             "Fingers and Tops": 0,
             "Five Finger Splay": 0,
             "Flange Spanner": 0,
             "Flaps Ahoy": 0,
             "Funbags": 0,
             "Gary's Gelding": 0,
             "Gentlmens Relish": 0,
             "Ginger Witch": 0,
             "Gypsy's Cat": 0,
             "Hairy Dyke": 0,
             "Handy Shandy": 0,
             "Hardly Flanged": 0,
             "Haway the Lads": 0,
             "Henrik's Jaw": 0,
             "Holy Colon": 0,
             "Hot Pants": 0,
             "Jackson's Lad": 0,
             "Jaques Yerlot": 0,
             "Jocks Away": 0,
             "Juice Trigger": 0,
             "Kelly's Boy": 0,
             "Kinnear's Demise": 0,
             "Knob Polisher": 0,
             "Knuckle Shuffle": 0,
             "Kohl Bunker": 0,
             "Les Long": 0,
             "Little Bishop": 0,
             "Lolly's Fern": 0,
             "Loose Pink": 0,
             "Lord Lucan": 0,
             "Love Burglar": 0,
             "Love Torpedo": 0,
             "Love Truncheon": 0,
             "Lush Gush": 0,
             "Money Shot": 0,
             "Mackem Delight": 0,
             "Mary Hinge": 0,
             "McTagnut & Fries": 0,
             "Melencholy Thatch": 0,
             "Monkey Puss": 0,
             "Monkey's Thumb": 0,
             "Mouse's Ear": 0,
             "Mr Winky": 0,
             "Neigh Bother": 0,
             "Neutered Nik": 0,
             "No Wasps": 0,
             "Ochayethenoo": 0,
             "One Eyed Warrior": 0,
             "Panhandle": 0,
             "Pearl's Necklace": 0,
             "Pearly Droplets": 0,
             "Pebbledash": 0,
             "Peking Twister": 0,
             "Piddle in Perspex": 0,
             "Pillow Biter": 0,
             "Priapism Willie": 0,
             "Purple Love": 0,
             "Reef's Folly": 0,
             "Reeves' Revenge": 0,
             "Ring of Fire": 0,
             "Rocinante": 0,
             "Rump Rider": 0,
             "Run Away Jay": 0,
             "Saddam's Madam": 0,
             "Salt 'n' Sauce": 0,
             "Sarwar's Spray": 0,
             "Sausage Sandwich": 0,
             "Schlong Odds": 0,
             "Scotland Nil": 0,
             "Shatner's Bassoon": 0,
             "Shoot Me": 0,
             "Silvery Tear": 0,
             "Skittery Trots": 0,
             "Slap & Tickle": 0,
             "Smellyama": 0,
             "Spam Javelin": 0,
             "Spicy Mushroom": 0,
             "Split Kipper": 0,
             "Stained Rigid": 0,
             "Sterilized Steed": 0,
             "Stool Pigeon": 0,
             "Syphilitic Meat": 0,
             "Tagnut": 0,
             "Tester Turd": 0,
             "That's Bollocks": 0,
             "The Angry Captain": 0,
             "Tight Brown": 0,
             "Tummy Squeaker": 0,
             "Tunky Packer": 0,
             "Tunnel Tester": 0,
             "Turbot Tornado": 0,
             "Up The Dumper": 0,
             "Uphill Gardner": 0,
             "Venereal Dodger": 0,
             "Vineger Stroke": 0,
             "Watery Passage": 0,
             "Weasel Burglar": 0,
             "Wee Crunchie": 0,
             "Wet Cabbage": 0,
             "Wet Circle": 0,
             "Wizard's Sleeve": 0,
             "Wong's Wang": 0,
             "Yoghurt Cannon": 0
             }

    def get_horse_list(self):
        return choices(list(self.NAMES), k=5)
