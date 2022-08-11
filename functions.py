import pygame
from settings import *


def load_sprite_sheet(filename):
    sprite_sheet = pygame.image.load(filename).convert_alpha()
    sprite_sheet = pygame.transform.scale(sprite_sheet, (TILESIZE * 17, TILESIZE))
    sprite_sheet_rect = sprite_sheet.get_rect()
    sprites = []
    for i in range(sprite_sheet_rect.width // TILESIZE):
        for j in range(sprite_sheet_rect.height // TILESIZE):
            rect = pygame.Rect((i * TILESIZE, j * TILESIZE), (TILESIZE, TILESIZE))
            sprites.append(sprite_sheet.subsurface(rect))
    return sprites
