SCALE_FACTOR = 4
TILESIZE = 16 * SCALE_FACTOR
WIDTH = 1600
HEIGHT = 900
FPS = 60
TITLE = "NEA Prototype"
BLACK = (0, 0, 0)
RED= (255, 0, 0)
MIN_ROOMS = 8
MAX_ROOMS = 12
MAX_DEPTH = 50
DUNGEON_SIZE = (16, 16)
POSSIBLE_ROOMS = {
        'N': ['NESW', 'S', 'NS', 'SW', 'ES', 'ESW', 'NSW', 'NES'],
        'S': ['NESW', 'N', 'NS', 'NW', 'NE', 'NEW', 'NSW', 'NES'],
        'E': ['NESW', 'W', 'EW', 'NW', 'SW', 'ESW', 'NSW', 'NEW'],
        'W': ['NESW', 'E', 'NE', 'ES', 'EW', 'ESW', 'NEW', 'NES'],
        }
