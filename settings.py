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
        'N': [['N', 'E', 'S', 'W'], ['S'], ['N', 'S'], ['S', 'W'], ['E', 'S'], ['E', 'S', 'W'], ['N', 'S', 'W'], ['N', 'E', 'S']],
        'E': [['N', 'E', 'S', 'W'], ['W'], ['E', 'W'], ['N', 'W'], ['S', 'W'], ['E', 'S', 'W'], ['N', 'S', 'W'], ['N', 'E', 'W']],
        'S': [['N', 'E', 'S', 'W'], ['N'], ['N', 'S'], ['N', 'W'], ['N', 'E'], ['N', 'E', 'W'], ['N', 'S', 'W'], ['N', 'E', 'S']],
        'W': [['N', 'E', 'S', 'W'], ['E'], ['N', 'E'], ['E', 'S'], ['E', 'W'], ['E', 'S', 'W'], ['N', 'E', 'W'], ['N', 'E', 'S']],
        }
