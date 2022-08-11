import pygame
from settings import *
import random


class Room:
    def __init__(self, game, paths, pos, room_type='normal'):
        self.game = game
        self.paths = paths
        self.pos = pos
        self.type = room_type
        self.image = self.assign_image()

    def assign_image(self):
        for key in self.game.room_path_dict:
            if self.paths == key:
                return self.game.room_path_dict[key]


class Dungeon:
    def __init__(self, game, size):
        self.game = game
        self.size = pygame.math.Vector2(size)
        self.num_rooms = 0

        w = int(self.size.x)
        h = int(self.size.y)

        self.rooms = [[None for _ in range(w)] for _ in range(h)]
        self.start_pos = [h // 2, w // 2]
        self.rooms[self.start_pos[0]][self.start_pos[1]] = Room(self.game, 'N', self.start_pos, 'spawn')
        self.new_room = None
        self.num_rooms += 1
        self.display_rooms()
        self.create_room(self.rooms[self.start_pos[0]][self.start_pos[1]])
        print(self.num_rooms)

    def create_room(self, room):
        free_paths = self.find_free_paths(room)
        self.num_rooms += 1
        while self.num_rooms < 12:
            if 'N' in free_paths and 'N' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['N']), [room.pos[0] - 1, room.pos[1]])
                self.rooms[room.pos[0] - 1][room.pos[1]] = self.new_room

            elif 'S' in free_paths and 'S' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['S']), [room.pos[0] + 1, room.pos[1]])
                self.rooms[room.pos[0] + 1][room.pos[1]] = self.new_room

            elif 'E' in free_paths and 'E' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['E']), [room.pos[0], room.pos[1] + 1])
                self.rooms[room.pos[0]][room.pos[1] + 1] = self.new_room

            elif 'W' in free_paths and 'W' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['W']), [room.pos[0], room.pos[1] - 1])
                self.rooms[room.pos[0]][room.pos[1] - 1] = self.new_room

            self.create_room(self.new_room)

    def find_free_paths(self, room):
        free_paths = []
        if self.rooms[room.pos[0]][room.pos[1] + 1] == None:
            free_paths.append('E')
        if self.rooms[room.pos[0]][room.pos[1] - 1] == None:
            free_paths.append('W')
        if self.rooms[room.pos[0] + 1][room.pos[1]] == None:
            free_paths.append('S')
        if self.rooms[room.pos[0] - 1][room.pos[1]] == None:
            free_paths.append('N')
        return free_paths


    def display_rooms(self):
        for row in range(len(self.rooms)):
            for col in range(len(self.rooms[row])):
                room = self.rooms[row][col]
                if room:
                    pos = (col * TILESIZE, row * TILESIZE)
                    self.game.screen.blit(room.image, pos)

    def update(self):
        self.display_rooms()
