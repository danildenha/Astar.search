import pygame
import math
from queue import PriorityQueue

WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Search by danildena")

#Color values for the nodes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (233, 30, 233)
ORANGE = (255, 135 ,0)
GREY = (140, 140, 140)
TURQUOISE = (48, 213, 200)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # Width = length since Node is square 
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows= total_rows



