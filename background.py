# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Filename:    const.py
# Created:     07/15/2019
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------

from sdl2 import SDL_CreateRGBSurface, \
    SDL_SWSURFACE, \
    SDL_BlitSurface, \
    SDL_Rect

from sdl2.ext import Resources, \
    load_image, \
    subsurface, \
    SoftwareSprite

import pyscroll
from pytmx.util_pysdl2 import load_pysdl2

from const import WindowSize

MAPS = Resources(__file__, 'resources', 'maps')


class Background:

    def __init__(self, filename, renderer):
        # Load TMX data
        self.tmx_data = load_pysdl2(filename=filename, renderer=renderer)

        # Make data source for the map
        self.map_data = pyscroll.TiledMapData(self.tmx_data)

        # Make the scrolling layer
        screen_size = (400, 400)
        map_layer = pyscroll.BufferedRenderer(self.map_data, screen_size)

        # make the pygame SpriteGroup with a scrolling map
        group = pyscroll.PyscrollGroup(map_layer=map_layer)

        # Add sprites to the group
        group.add(sprite)

        # Center the layer and sprites on a sprite
        group.center(sprite.rect.center)

        # Draw the layer
        # If the map covers the entire screen, do not clear the screen:
        # Clearing the screen is not needed since the map will clear it when drawn
        # This map covers the screen, so no clearing!
        group.draw(screen)

        # adjust the zoom (out)
        map_layer.zoom = .5

        # adjust the zoom (in)
        map_layer.zoom = 2.0
