# -*- coding: utf-8 -*-

from sdl2 import SDL_BlitSurface, \
    SDL_CreateRGBSurface, \
    SDL_SWSURFACE, \
    SDL_Rect

from sdl2.ext import Resources, \
    SoftwareSprite, \
    load_image, \
    subsurface

from components.motion import MotionType

from logging import getLogger

RESOURCES = Resources(__file__, 'resources')
LOG = getLogger(__name__)


class SpriteSheet:
    """ Sprite sheet """

    def __init__(self, name, width, height, count):
        super(SpriteSheet, self).__init__()

        self.name = name

        self.frame = 0

        self.motion_types = MotionType().get_all()
        self.motion_type = 0

        self.facing = 0

        self.sprite = None
        self.sprite_surface = None

        self.sprite_size = width, height

        self.sprites_path = {}

        self.images = {}
        self.surfaces = {}
        self.surfaces_size = {}
        self.surfaces_with = []
        self.surfaces_height = 0

        for k, v in self.motion_types.items():
            LOG.debug(f"filename {self.name}_{k}.png")
            path = RESOURCES.get_path(f"{self.name}_{k}.png")

            mt = self.motion_types[k]
            LOG.debug(f"motion_type: {mt}")
            # for k, v in self.sprites_path.items():
            self.images[mt] = load_image(path)
            self.surfaces_size[mt] = self.images[mt].w, self.images[mt].h
            self.surfaces_with = self.images[mt].w
            self.surfaces_height = self.images[mt].h

            LOG.debug(f"WIDHT {self.surfaces_with}")
            LOG.debug(f"HEIGHT {self.surfaces_height}")

            new_surface = SDL_CreateRGBSurface(SDL_SWSURFACE,
                                               self.surfaces_with,
                                               self.surfaces_height,
                                               32,
                                               0x000000FF,
                                               0x0000FF00,
                                               0x00FF0000,
                                               0xFF000000)

            i = 0
            for filename, surface in self.images.items():
                vertical_offset = i * self.images[filename].h
                rect = SDL_Rect(0, vertical_offset, self.images[filename].w, self.images[filename].h)
                SDL_BlitSurface(surface, None, new_surface, rect)
                i += 1
            self.surfaces[mt] = new_surface

        LOG.debug(f"SURFACE {self.surfaces}")

    def get_surface(self, frame, motion_type, facing):

        self.frame = frame
        self.motion_type = motion_type
        self.facing = facing

        w, h = self.sprite_size

        crop = (w * self.frame, 0, w, h)

        self.sprite_surface = subsurface(self.images[self.motion_type], crop)

        return self.sprite_surface

    def get_sprite(self):
        surface = self.get_surface(0, 0, 0)
        return SoftwareSprite(surface, True)

    def get_sprite_sheet_width(self, motion_type):
        return self.images[motion_type].w

    def get_sprite_size(self):
        return self.sprite_size
