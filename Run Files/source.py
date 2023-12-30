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

    #GET STATE OF THE NODE
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_obstacle(self):
        return self.color == BLACK
    
    def is_begin(self):
        return self.color == TURQUOISE
    
    def is_end(self):
        return self.color == PURPLE
    
     #MAKE CHANGES TO THE NODE
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_obstacle(self):
        self.color = BLACK
    
    def make_begin(self):
        self.color = TURQUOISE
    
    def make_end(self):
        self.color = PURPLE
    
    def reset(self):
        self.color = WHITE

    def make_path(self):
        self.color = ORANGE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def add_neighbours(self, grid):
        pass

    def __lt__(self, other):
         return False

#heuristic function using manhattan distance formula
def heuristic(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + (y1 - y2)

#only rows since columns = rows
def grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):

