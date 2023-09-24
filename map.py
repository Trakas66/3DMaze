import pygame
from mazegenerator import *

mini_map = mazeArray()

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            pygame.draw.rect(self.game.screen, 'darkgray', (pos[0]*15, pos[1]*15, 15, 15), 2)