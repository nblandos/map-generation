import sys
import pygame
from settings import *
import functions as f
import dungeon_generator as dg


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.room_images = None
        self.load_assets()
        self.dungeon = dg.Dungeon(self, DUNGEON_SIZE)
        self.screen.fill(BLACK)

    def load_assets(self):
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
        self.screen.fill(BLACK)
        self.dungeon = dg.Dungeon(self, DUNGEON_SIZE)

    def update(self):
        self.dungeon.update()

    def run(self):
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
