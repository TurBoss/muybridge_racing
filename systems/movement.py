# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Filename:    movement.py
# Created:     07/2/2019
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------
import random

from sdl2.ext import Applicator, Sprite

from components.velocity import Velocity


class MovementSystem(Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = Velocity, Sprite

        self.minx = minx
        self.miny = miny

        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:

            # swidth, sheight = sprite.size

            if velocity.vx > 0:
                sprite.x += random.randint(0, 3)

            sprite.x += velocity.vx
            sprite.y += velocity.vy

            # sprite.x = max(self.minx, sprite.x)
            # sprite.y = max(self.miny, sprite.y)
            #
            # pmaxx = sprite.x + swidth
            # pmaxy = sprite.y + sheight
            # if pmaxx > self.maxx:
            #     sprite.x = self.maxx - swidth
            # if pmaxy > self.maxy:
            #     sprite.y = self.maxy - sheight
