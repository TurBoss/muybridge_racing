# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Filename:    const.py
# Created:     03/16/2017
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------

from sdl2 import SDL_GetTicks, \
    SDL_KEYUP, \
    SDL_KEYDOWN, \
    SDL_QUIT, \
    SDL_Delay, \
    SDLK_ESCAPE, \
    SDLK_SPACE

from sdl2.ext import Resources, \
    get_events

from background import Background
from const import WindowSize
from db import DataBase
from input import Input
from horse import Horse

from spritesheet import SpriteSheet
from systems.animation import AnimationSystem
from systems.movement import MovementSystem

FPS = 30  # units.FPS
MAX_FRAME_TIME = int(5 * (1000 / FPS))

RESOURCES = Resources(__file__, 'resources')
MAPS = Resources(__file__, 'resources', 'maps')


class Game:
    def __init__(self, world, window, renderer, factory):

        self.db = DataBase()

        self.running = False
        self.race_running = False

        self.world = world
        self.window = window
        self.renderer = renderer
        self.factory = factory

        # self.background = Background(self.world, self.renderer, "map.tmx")

        self.sprites = []

        sprite_sheet_1 = SpriteSheet("daisy", 128, 90, 16)
        sprite_sheet_2 = SpriteSheet("daisy", 128, 90, 16)
        sprite_sheet_3 = SpriteSheet("daisy", 128, 90, 16)
        sprite_sheet_4 = SpriteSheet("daisy", 128, 90, 16)
        sprite_sheet_5 = SpriteSheet("daisy", 128, 90, 16)

        self.horse_1 = Horse(self.world, sprite_sheet_1, 128, 256)
        self.horse_2 = Horse(self.world, sprite_sheet_2, 128, 256 + 100)
        self.horse_3 = Horse(self.world, sprite_sheet_3, 128, 256 + 200)
        self.horse_4 = Horse(self.world, sprite_sheet_4, 128, 256 + 300)
        self.horse_5 = Horse(self.world, sprite_sheet_5, 128, 256 + 400)

        self.horse_1.motiontype.set("running")
        self.horse_2.motiontype.set("standing")
        self.horse_3.motiontype.set("standing")
        self.horse_4.motiontype.set("standing")
        self.horse_5.motiontype.set("standing")

        x = int(WindowSize.WIDTH / 2)
        y = int(WindowSize.HEIGHT / 2)

        self.horse_1_anim = AnimationSystem(self.horse_1, sprite_sheet_1)

        self.movement = MovementSystem(0, 0, 1024, 768)

        # self.all_horses = [Enemy(self.renderer, self.factory, "doombat")]

        self.world.add_system(self.movement)

        self.world.add_system(self.horse_1_anim)

        self.world.add_system(self.renderer)

    def start_race(self):
        if not self.race_running:
            self.race_running = True

            self.horse_1.motiontype.set("running")

            self.horse_1.velocity.vx = 3
            self.horse_2.velocity.vx = 3
            self.horse_3.velocity.vx = 3
            self.horse_4.velocity.vx = 3
            self.horse_5.velocity.vx = 3

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

        # speed_x, speed_y = 2, 1
        # player_pos = [-100, -100]

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
                    self.clear()
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

            # Start
            if game_input.was_key_pressed(SDLK_SPACE):
                self.start_race()

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

        self.horse_1.delete()
        self.horse_2.delete()
        self.horse_3.delete()
        self.horse_4.delete()
        self.horse_5.delete()
        # self.sky_background.delete()
        # self.mountains_background.delete()
        # self.floor_background.delete()

        self.world.remove_system(self.horse_1_anim)
        self.world.remove_system(self.movement)
