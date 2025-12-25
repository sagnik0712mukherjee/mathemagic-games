# Snake Game Settings
HEIGHT = 300
WIDTH = 300
GRID_SIZE = 5
FPS = 20
CELL_SIZE = WIDTH // GRID_SIZE

# Colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Actions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
ACTIONS = [UP, DOWN, LEFT, RIGHT]

# Q-Learning Parameters
ALPHA = 0.1  # learning rate
GAMMA = 0.9  # discount factor
EPSILON = 0.2  # exploration rate
NUM_EPISODES = 5000
