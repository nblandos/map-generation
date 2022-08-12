import pygame
from settings import *
import random


class Room:
    def __init__(self, game, paths, pos, room_type='normal'):
        self.game = game
        self.paths = paths
        self.pos = pos
        self.type = room_type
        self.image = None
        self.text = self.assign_text()

    def assign_image(self):
        for key in self.game.room_path_dict:
            if self.paths == key:
                return self.game.room_path_dict[key]

    def assign_text(self):
        if self.type == 'normal':
            return None
        elif self.type == 'spawn':
            return 'Spawn'


class Dungeon:
    def __init__(self, game, size):
        self.game = game
        self.size = pygame.math.Vector2(size)
        self.num_rooms = 0
        self.spawned = False

        w = int(self.size.x)
        h = int(self.size.y)
        self.rooms = [[None for _ in range(w)] for _ in range(h)]
        self.start_pos = [h // 2, w // 2]
        self.depth = 0
        self.new_room = None
        self.generate_dungeon()

    def generate_dungeon(self):
        self.rooms[self.start_pos[0]][self.start_pos[1]] = Room(self.game, 'N', self.start_pos, 'spawn')
        self.create_room(self.rooms[self.start_pos[0]][self.start_pos[1]])
        self.create_connections()


    def create_room(self, room):
        self.depth += 1
        free_paths = self.find_free_paths(room)

        if not self.spawned and len(free_paths) > 0 and self.depth < MAX_DEPTH:
            if 'N' in free_paths and 'N' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['N']), [room.pos[0] - 1, room.pos[1]])
                self.rooms[room.pos[0] - 1][room.pos[1]] = self.new_room

            if 'S' in free_paths and 'S' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['S']), [room.pos[0] + 1, room.pos[1]])
                self.rooms[room.pos[0] + 1][room.pos[1]] = self.new_room

            if 'E' in free_paths and 'E' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['E']), [room.pos[0], room.pos[1] + 1])
                self.rooms[room.pos[0]][room.pos[1] + 1] = self.new_room

            if 'W' in free_paths and 'W' in room.paths:
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS['W']), [room.pos[0], room.pos[1] - 1])
                self.rooms[room.pos[0]][room.pos[1] - 1] = self.new_room

            self.create_room(self.new_room)
            self.spawned = True

    def count_rooms(self):
        num_rooms = 0
        for row in self.rooms:
            for room in row:
                if room:
                    num_rooms += 1
        return num_rooms

    def find_free_paths(self, room):
        free_paths = []
        if room.pos[1] + 1 > self.size.x - 1:
            pass
        elif self.rooms[room.pos[0]][room.pos[1] + 1] is None:
            free_paths.append('E')
        if room.pos[1] - 1 < 0:
            pass
        elif self.rooms[room.pos[0]][room.pos[1] - 1] is None:
            free_paths.append('W')
        if room.pos[0] + 1 > self.size.y - 1:
            pass
        elif self.rooms[room.pos[0] + 1][room.pos[1]] is None:
            free_paths.append('S')
        if room.pos[0] - 1 < 0:
            pass
        elif self.rooms[room.pos[0] - 1][room.pos[1]] is None:
            free_paths.append('N')
        return free_paths

    def display_rooms(self):
        for row in range(len(self.rooms)):
            for col in range(len(self.rooms[row])):
                room = self.rooms[row][col]
                if room:
                    pos = (col * TILESIZE, row * TILESIZE)
                    self.game.screen.blit(room.image, pos)
                    # TODO show text on room for room type

    def create_connections(self):
        for row in self.rooms:
            for room in row:
                if room:
                    room.paths = ''
                    if room.pos[0] - 1 < 0:
                        pass
                    elif self.rooms[room.pos[0] - 1][room.pos[1]] is not None:
                        room.paths += 'N'

                    if room.pos[1] + 1 > self.size.x - 1:
                        pass
                    elif self.rooms[room.pos[0]][room.pos[1] + 1] is not None:
                        room.paths += 'E'

                    if room.pos[0] + 1 > self.size.y - 1:
                        pass
                    elif self.rooms[room.pos[0] + 1][room.pos[1]] is not None:
                        room.paths += 'S'

                    if room.pos[1] - 1 < 0:
                        pass
                    elif self.rooms[room.pos[0]][room.pos[1] - 1] is not None:
                        room.paths += 'W'
                    room.image = room.assign_image()

    def update(self):
        self.display_rooms()
