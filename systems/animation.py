# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Filename:    player_animation.py
# Created:     03/16/2017
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------

from sdl2 import SDL_BlitSurface, \
    SDL_Rect, \
    SDL_FillRect

from sdl2.ext import Applicator, \
    Sprite

from components.frames import Frames
from components.motion import MotionType
from components.facing import Facing

from horse import HorseData


class AnimationSystem(Applicator):
    def __init__(self, horse, sprite_sheet):
        super(AnimationSystem, self).__init__()
        self.componenttypes = HorseData, Frames, MotionType, Facing, Sprite

        self.horse = horse
        self.sprite_sheet = sprite_sheet

        self.motion_type = "standing"
        self.facing = "down"
        self.last_facing = self.facing
        self.last_motion_type = self.motion_type

        self.surface = None
        self.sprite_surface = None

    def process(self, world, componentsets):
        for horsedata, frames, motion_type, facing, sprite in componentsets:
            self.facing = facing.get()
            self.motion_type = motion_type.get()



            count = 16

            if self.motion_type == 0:
                count = 2
            elif self.motion_type == 1:
                count = 16

            if (self.facing != self.last_facing) or (self.motion_type != self.last_motion_type):
                frames.set(0)

            width = self.sprite_sheet.get_sprite_sheet_width(motion_type.get())

            if frames.get() == width / count:
                frames.set(0)

            self.surface = self.sprite_sheet.get_surface(frames.get(), motion_type.get(), facing.get())
            self.sprite_surface = sprite.surface

            h, w = self.sprite_sheet.get_sprite_size()
            rect = SDL_Rect(0, 0, w, h)
            SDL_FillRect(self.sprite_surface, None, 0x000000)
            SDL_BlitSurface(self.surface, None, self.sprite_surface, rect)

            self.last_facing = self.facing
            self.last_motion_type = self.motion_type

            if frames.get() > count:
                frames.set(0)
            else:
                frames.bump()


