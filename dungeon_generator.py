# Imports necessary modules
import pygame
import random
# Settings contains the constants used in the game
from settings import *


# Defines the Room class
class Room:
    def __init__(self, game, paths, pos, room_type='normal'):
        # Initializes the Room class
        self.game = game
        self.paths = paths
        self.free_paths = []
        self.pos = pos
        self.type = room_type
        # None is assigned to image as connections are not yet correctly assigned
        self.image = None
        # Room type remains the same so text can be initialized
        self.text = self.assign_text()

    def assign_image(self):
        # Assigns the image for each room based on its connections
        for key in self.game.room_path_dict:
            if self.paths == key:
                return self.game.room_path_dict[key]

    def assign_text(self):
        # Assigns the text for each room based on its type
        if self.type == 'normal':
            return None
        elif self.type == 'spawn':
            return 'S'


# Defines the Dungeon class
class Dungeon:
    def __init__(self, game, size):
        # Initializes the Dungeon class
        self.game = game
        self.size = pygame.math.Vector2(size)
        w = int(self.size.x)
        h = int(self.size.y)
        self.num_rooms = 0
        # Creates an empty 2D array that will store the rooms
        self.rooms = [[None for _ in range(w)] for _ in range(h)]
        self.start_pos = [h // 2, w // 2]
        self.new_pos = None
        self.new_room = None
        self.generate_dungeon()

    def generate_dungeon(self):
        # Creates the spawn room
        self.rooms[self.start_pos[0]][self.start_pos[1]] = Room(self.game, ['N'], self.start_pos, 'spawn')
        # Calls the necessary functions to generate the dungeon
        self.create_room(self.rooms[self.start_pos[0]][self.start_pos[1]])
        self.create_connections()

    def create_room(self, room):
        # Main function that creates the dungeon
        free_paths = self.find_free_paths(room)
        # Uses a set to remove the paths that have been randomly chosen but are not free
        available_paths = (list(set(free_paths).intersection(room.paths)))
        if available_paths:
            # Shuffles so that the paths are not always chosen in the same order
            random.shuffle(available_paths)
            # Loops through the available generated paths and assigns the new room coordinates
            for path in available_paths:
                if path == 'N':
                    self.new_pos = [room.pos[0] - 1, room.pos[1]]
                elif path == 'E':
                    self.new_pos = [room.pos[0], room.pos[1] + 1]
                elif path == 'S':
                    self.new_pos = [room.pos[0] + 1, room.pos[1]]
                elif path == 'W':
                    self.new_pos = [room.pos[0], room.pos[1] - 1]
                # Instantiates the new room and adds it to the 2D array 'rooms'
                self.new_room = Room(self.game, random.choice(POSSIBLE_ROOMS[path]), self.new_pos)
                self.rooms[self.new_pos[0]][self.new_pos[1]] = self.new_room
                # Recursively calls the function to explore the newly created room and create its neighbours
                self.create_room(self.new_room)


    def count_rooms(self):
        # Returns the number of rooms in the dungeon
        num_rooms = 0
        for row in self.rooms:
            for room in row:
                if room:
                    num_rooms += 1
        return num_rooms

    def display_rooms(self):
        # Loops through the 2D array and displays the rooms
        font = pygame.font.SysFont('Arial', 48)
        for row in range(len(self.rooms)):
            for col in range(len(self.rooms[row])):
                room = self.rooms[row][col]
                if room:
                    pos = (col * TILESIZE, row * TILESIZE)
                    text_pos = (pos[0] + TILESIZE // 3, pos[1] + TILESIZE // 9)
                    text = font.render(room.text, True, RED)
                    self.game.screen.blit(room.image, pos)
                    self.game.screen.blit(text, text_pos)

    def create_connections(self):
        """Loops through the 2D array and re-assigns the connections for each room.
        This is necessary because the connections are randomized when the rooms are created and sometimes
        left un-explored due to MAX_DEPTH. Without this function, There would be many paths that lead nowhere."""
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

    def find_free_paths(self, room):
        free_paths = []
        # Returns a list of free paths for the current room
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

    def update(self):
        # Code here is called every frame
        self.display_rooms()
