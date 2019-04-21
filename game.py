# -*- coding: utf-8 -*-

from sdl2 import SDL_GetTicks, \
    SDL_KEYUP, \
    SDL_KEYDOWN, \
    SDL_QUIT, \
    SDL_Delay,\
    SDLK_ESCAPE, \
    SDLK_RIGHT, \
    SDLK_UP, \
    SDLK_DOWN, \
    SDLK_LEFT, \
    SDLK_SPACE

from sdl2.ext import Resources, \
    get_events

from const import WindowSize
from db import DataBase
from input import Input
from horse import Horse

from components.spritesheet import SpriteSheet
from systems.animation import AnimationSystem
from systems.movement import MovementSystem

FPS = 16  # units.FPS
MAX_FRAME_TIME = int(5 * (1000 / FPS))

RESOURCES = Resources(__file__, 'resources')
MAPS = Resources(__file__, 'resources', 'maps')


class Game:
    def __init__(self, world, window, renderer, factory):

        self.db = DataBase()

        self.running = False
        self.world = world
        self.window = window
        self.renderer = renderer
        self.factory = factory

        self.background_tiles = []
        self.behind_tiles = []
        self.front_tiles = []
        self.sprites = []

        x = int(WindowSize.WIDTH / 2)
        y = int(WindowSize.HEIGHT / 2)

        self.all_npc = []

        self.horse_sprite_sheet = SpriteSheet("daisy")
        self.horse_sprite = self.horse_sprite_sheet.get_sprite()

        self.horse_1 = Horse(self.world, self.horse_sprite, 0, 0)

        self.horse_animation = AnimationSystem("daisy")
        self.horse_movement = MovementSystem(x - 128, y - 128, x + 128, y + 128)
        # self.all_enemies = [Enemy(self.renderer, self.factory, "doombat")]

        self.world.add_system(self.horse_animation)
        self.world.add_system(self.horse_movement)

        self.world.add_system(self.renderer)

    def init_map(self, map_name):

        map_data = self.db.get_map_npc(map_name)
        map_npc = []

        for data in map_data:
            map_npc.append(data["npc"])
            print(data)

        # for npc in map_npc:
        #    self.all_npc.append(NPC(self.renderer, self.factory, npc))
    """
    def get_sprites(self):

        self.sprites.append(self.map_background_sprite)
        # self.sprites.append(self.map_behind_sprite)

        # self.sprites.append(self.map_front_sprite)

        for npc in self.all_npc:
            for sprite in npc.get_sprites():
                self.sprites.append(sprite)

        for enemy in self.all_enemies:
            for sprite in enemy.get_sprites():
                self.sprites.append(sprite)

    def update(self, position, motion_type, facing, elapsed_time):

        self.map_background_sprite.position = position
        # self.map_behind_sprite.position = position

        # self.player.update(motion_type, facing, elapsed_time)

        for npc in self.all_npc:
            npc.update(position, elapsed_time)

        for enemy in self.all_enemies:
            enemy.update(position, elapsed_time)
    """

    def run(self):

        game_input = Input()

        speed_x, speed_y = 2, 1
        player_pos = [-100, -100]

        # motion_type = self.player_motion_type
        # facing = self.player_facing

        self.running = True
        last_update_time = SDL_GetTicks()  # units.MS

        while self.running:
            start_time = SDL_GetTicks()  # units.MS

            game_input.begin_new_frame()
            game_events = get_events()

            for event in game_events:
                if event.type == SDL_KEYDOWN:
                    game_input.key_down_event(event)

                elif event.type == SDL_KEYUP:
                    game_input.key_up_event(event)

                elif event.type == SDL_QUIT:
                    self.running = False
                    break

            if not self.running:
                self.clear()
                break

            # Exit
            if game_input.was_key_pressed(SDLK_ESCAPE):
                self.clear()
                self.running = False
                break

            # # Player movement
            # if game_input.is_key_held(SDLK_RIGHT) and game_input.is_key_held(SDLK_UP):
            #     player_pos[0] -= speed_x
            #     player_pos[1] += speed_y
            #     self.horse.velocity.vx = speed_x
            #     self.horse.velocity.vy = -speed_y
            #     self.horse.facing.set("right_up")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_RIGHT) and game_input.is_key_held(SDLK_DOWN):
            #     player_pos[0] -= speed_x
            #     player_pos[1] -= speed_y
            #     self.horse.velocity.vx = speed_x
            #     self.horse.velocity.vy = speed_y
            #     self.horse.facing.set("right_down")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_LEFT) and game_input.is_key_held(SDLK_UP):
            #     player_pos[0] += speed_x
            #     player_pos[1] += speed_y
            #     self.horse.velocity.vx = -speed_x
            #     self.horse.velocity.vy = -speed_y
            #     self.horse.facing.set("left_up")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_LEFT) and game_input.is_key_held(SDLK_DOWN):
            #     player_pos[0] += speed_x
            #     player_pos[1] -= speed_y
            #     self.horse.velocity.vx = -speed_x
            #     self.horse.velocity.vy = speed_y
            #     self.horse.facing.set("left_down")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_LEFT):
            #     player_pos[0] += speed_x
            #     self.horse.velocity.vx = -speed_x
            #     self.horse.facing.set("left")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_RIGHT):
            #     player_pos[0] -= speed_x
            #     self.horse.velocity.vx = speed_x
            #     self.horse.facing.set("right")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_UP):
            #     player_pos[1] += speed_y
            #     self.horse.velocity.vy = -speed_y
            #     self.horse.facing.set("up")
            #     self.horse.motiontype.set("walking")
            # elif game_input.is_key_held(SDLK_DOWN):
            #     player_pos[1] -= speed_y
            #     self.horse.velocity.vy = speed_y
            #     self.horse.facing.set("down")
            #     self.horse.motiontype.set("walking")

            # elif game_input.was_key_pressed(SDLK_i):
            #    self.player.toggle_inventory()

            # Player Attack
            elif game_input.is_key_held(SDLK_SPACE):

                self.horse_1.velocity.vx = 1
                self.horse_1.velocity.vy = 0
                self.horse_1.motiontype.set("running")

            current_time = SDL_GetTicks()  # units.MS
            elapsed_time = current_time - last_update_time  # units.MS

            last_update_time = current_time

            self.world.process()

            # This loop lasts 1/60th of a second, or 1000/60th ms
            ms_per_frame = 1000 // FPS  # units.MS
            elapsed_time = SDL_GetTicks() - start_time  # units.MS
            if elapsed_time < ms_per_frame:
                SDL_Delay(ms_per_frame - elapsed_time)

    def clear(self):
        self.horse.delete()
        self.npc.delete()

        self.world.remove_system(self.player_animation)
        self.world.remove_system(self.npc_animation)

        self.world.remove_system(self.player_movement)
        self.world.remove_system(self.npc_movement)
