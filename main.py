import sys
from random import randint

import sdl2
import sdl2.ext

from renderer_systems import SoftwareRenderer, TextureRenderer

WHITE = sdl2.ext.Color(255, 255, 255)
GREEN = sdl2.ext.Color(0, 255, 0)
RESOURCES = sdl2.ext.Resources(__file__, "resources")


# This can be either "software" or "texture"
RENDERER = "texture"


class MovementSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight


class CollisionSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.ball = None
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def _overlap(self, item):
        pos, sprite = item
        if sprite == self.ball.sprite:
            return False

        left, top, right, bottom = sprite.area
        bleft, btop, bright, bbottom = self.ball.sprite.area

        return (bleft < right and bright > left and
                btop < bottom and bbottom > top)

    def process(self, world, componentsets):
        collitems = [comp for comp in componentsets if self._overlap(comp)]
        if collitems:
            self.ball.velocity.vx = -self.ball.velocity.vx


class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0


class TrackingAIController(sdl2.ext.Applicator):
    def __init__(self, min_x, max_x):
        super(TrackingAIController, self).__init__()
        self.componenttypes = PlayerData, Velocity, sdl2.ext.Sprite
        self.min_x = min_x
        self.max_x = max_x
        self.player = None

    def process(self, world, componentsets):
        velocity = randint(-3, 3)
        self.player.velocity.vx = velocity


class BackgroundController(sdl2.ext.Applicator):
    def __init__(self, min_x, max_x):
        super(BackgroundController, self).__init__()
        self.componenttypes = BackgroundData, Velocity, sdl2.ext.Sprite
        self.min_x = min_x
        self.max_x = max_x
        self.bg = None

    def process(self, world, componentsets):
        velocity = -3
        self.bg.velocity.vx = velocity


class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.ai = False


class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0, ai=True):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        self.playerdata = PlayerData()
        self.playerdata.ai = ai

class BackgroundData(object):
    def __init__(self):
        super(BackgroundData, self).__init__()


class Background(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        self.backgrounddata = BackgroundData()


def run():

    sdl2.ext.init()

    window = sdl2.ext.Window("Muybridge Racing", size=(800, 600))
    window.show()

    world = sdl2.ext.World()

    spriterenderer = None
    texture_renderer = None
    factory = None

    # Set up our renderer.
    if RENDERER == "software":
        spriterenderer = SoftwareRenderer(window)
    elif RENDERER == "texture":
        texture_renderer = sdl2.ext.Renderer(window)
        spriterenderer = TextureRenderer(texture_renderer)

    # Create our paddle sprites from our sprite factory.
    if RENDERER == "software":
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    elif RENDERER == "texture":
        factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=texture_renderer)

    movement = MovementSystem(0, 0, 800, 600)

    bg = factory.from_image(RESOURCES.get_path("floor.png"))


    horse_1 = factory.from_image(RESOURCES.get_path("daisy.png"))
    horse_2 = factory.from_image(RESOURCES.get_path("daisy.png"))
    horse_3 = factory.from_image(RESOURCES.get_path("daisy.png"))
    horse_4 = factory.from_image(RESOURCES.get_path("daisy.png"))
    horse_5 = factory.from_image(RESOURCES.get_path("daisy.png"))

    background = Background(world, bg, 0, 200)

    player_1 = Player(world, horse_1, 390, 170)
    player_2 = Player(world, horse_2, 390, 260)
    player_3 = Player(world, horse_3, 390, 350)
    player_4 = Player(world, horse_4, 390, 440)
    player_5 = Player(world, horse_5, 390, 530)

    bgcontroller = BackgroundController(0, 800)

    aicontroller_1 = TrackingAIController(0, 800)
    aicontroller_2 = TrackingAIController(0, 800)
    aicontroller_3 = TrackingAIController(0, 800)
    aicontroller_4 = TrackingAIController(0, 800)
    aicontroller_5 = TrackingAIController(0, 800)

    bgcontroller.bg = background

    aicontroller_1.player = player_1
    aicontroller_2.player = player_2
    aicontroller_3.player = player_3
    aicontroller_4.player = player_4
    aicontroller_5.player = player_5

    world.add_system(bgcontroller)

    world.add_system(aicontroller_1)
    world.add_system(aicontroller_2)
    world.add_system(aicontroller_3)
    world.add_system(aicontroller_4)
    world.add_system(aicontroller_5)

    world.add_system(movement)

    world.add_system(spriterenderer)

    running = True

    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_LEFT:
                    pass
                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    pass
            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_RIGHT, sdl2.SDLK_LEFT):
                    pass

        if RENDERER == "texture":
            texture_renderer.clear()

        world.process()

        sdl2.SDL_Delay(30)


if __name__ == "__main__":
    sys.exit(run())
