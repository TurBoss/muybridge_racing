# -*- coding: utf-8 -*-

from sdl2 import SDL_CreateRGBSurface, SDL_SWSURFACE, SDL_Rect, SDL_BlitSurface
from sdl2.ext import Resources, Entity, load_image, SoftwareSprite

from components.velocity import Velocity

RESOURCES = Resources(__file__, 'resources')


class Background(Entity):
    """ Background """

    def __init__(self, world, posx, posy, width, height, mame):
        super(Background, self).__init__()

        self.frame = 0
        self.velocity = Velocity()

        tile = "{}.png".format(mame)

        sprite_path = RESOURCES.get_path(tile)

        tile_surface = load_image(sprite_path)

        surface = SDL_CreateRGBSurface(SDL_SWSURFACE,
                                            1920,
                                            768,
                                            32,
                                            0x000000FF,
                                            0x0000FF00,
                                            0x00FF0000,
                                            0xFF000000)

        rect = SDL_Rect(posx, posy, width, height)
        SDL_BlitSurface(tile_surface, None, surface, rect)

        self.sprite = SoftwareSprite(surface.contents, True)
