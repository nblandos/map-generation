import sys
import pygame
from settings import *
import functions as f
import dungeon_generator as dg

# Defines the Game class
class Game:
    def __init__(self):
        # Initializes the Game class
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.room_images = None
        self.room_path_dict = None
        self.dungeon = None
        self.reset()

    def load_assets(self):
        # Loads the room images from the sprite sheet
        self.room_images = f.load_sprite_sheet("assets/room_strip_opaque.png")
        self.room_path_dict = {
            'NESW': self.room_images[0],
            'EW': self.room_images[1],
            'NS': self.room_images[2],
            'S': self.room_images[3],
            'N': self.room_images[4],
            'W': self.room_images[5],
            'E': self.room_images[6],
            'NSW': self.room_images[7],
            'ESW': self.room_images[8],
            'NES': self.room_images[9],
            'NEW': self.room_images[10],
            'NW': self.room_images[11],
            'SW': self.room_images[12],
            'ES': self.room_images[13],
            'NE': self.room_images[14],
            'green': self.room_images[15],
            'red': self.room_images[16]
        }

    def reset(self):
        # Initializes a new dungeon
        self.load_assets()
        self.screen.fill(BLACK)
        self.dungeon = dg.Dungeon(self, DUNGEON_SIZE)
        # Dungeons are generated until the number of rooms is between a certain range and there is only one connection to the spawn room
        while self.dungeon.count_rooms() < MIN_ROOMS or self.dungeon.count_rooms() > MAX_ROOMS or len(self.dungeon.rooms[self.dungeon.start_pos[0]][self.dungeon.start_pos[1]].paths) != 1:
            self.dungeon = dg.Dungeon(self, DUNGEON_SIZE)

    def update(self):
        self.dungeon.update()

    def run(self):
        # Game loop called every frame
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()

            pygame.display.update()

            self.clock.tick(FPS)
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()
