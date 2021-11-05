#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------
# Filename:    main.py
# Created:     03/16/2017
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------

import logging

from sdl2 import SDL_Rect, \
    SDL_RenderCopyEx, \
    SDL_FLIP_NONE, \
    SDL_RenderPresent, \
    SDL_Init, \
    SDL_INIT_EVERYTHING

from sdl2.ext import Window, \
    Renderer, \
    fill, \
    SoftwareSpriteRenderSystem, \
    TextureSpriteRenderSystem, \
    Color, \
    SDLError, \
    World, \
    SOFTWARE, \
    TEXTURE, \
    SpriteFactory

from sdl2.ext.compat import isiterable

from const import WindowSize
from menu import Menu

# This can be either "software" or "texture"
RENDERER = "software"

logging.basicConfig(level=logging.DEBUG)

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class SoftwareRenderer(SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, sprites, x=None, y=None):
        # Fill the screen with black every frame.
        fill(self.surface, Color(0, 0, 0))
        super(SoftwareRenderer, self).render(sprites)


class TextureRenderer(TextureSpriteRenderSystem):
    def __init__(self, target):
        super(TextureRenderer, self).__init__(target)

    def render(self, sprites, x=None, y=None):
        """Overrides the render method of sdl2.ext.TextureSpriteRenderSystem to
        use "SDL_RenderCopyEx" instead of "SDL_RenderCopy" to allow sprite
        rotation:
        http://wiki.libsdl.org/SDL_RenderCopyEx
        """
        r = SDL_Rect(0, 0, 0, 0)
        if isiterable(sprites):
            rcopy = SDL_RenderCopyEx
            renderer = self.sdlrenderer
            x = x or 0
            y = y or 0
            for sp in sprites:
                r.x = x + sp.x
                r.y = y + sp.y
                r.w, r.h = sp.size
                if rcopy(renderer, sp.texture, None, r, sp.angle, None, SDL_FLIP_NONE) == -1:
                    raise SDLError()
        else:
            r.x = sprites.x
            r.y = sprites.y
            r.w, r.h = sprites.size
            if x is not None and y is not None:
                r.x = x
                r.y = y
            SDL_RenderCopyEx(self.sdlrenderer,
                             sprites.texture,
                             None,
                             r,
                             sprites.angle,
                             None,
                             SDL_FLIP_NONE)

        SDL_RenderPresent(self.sdlrenderer)


def main():
    LOG.debug("INIT")
    screen_size = WindowSize.WIDTH, WindowSize.HEIGHT

    SDL_Init(SDL_INIT_EVERYTHING)

    window = Window("CyberMotor3000", screen_size)
    window.show()

    world = World()

    sprite_renderer = None
    texture_renderer = None

    if RENDERER == "software":
        sprite_renderer = SoftwareRenderer(window)
    elif RENDERER == "texture":
        texture_renderer = Renderer(window)
        sprite_renderer = TextureRenderer(texture_renderer)

    factory = None
    if RENDERER == "software":
        factory = SpriteFactory(SOFTWARE)
    elif RENDERER == "texture":
        factory = SpriteFactory(TEXTURE, renderer=texture_renderer)

    menu = Menu(window, world, sprite_renderer, factory)
    menu.run()


if __name__ == '__main__':
    main()
