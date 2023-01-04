from pygame.sprite import *
import pygame
import random

class Piece(pygame.sprite.Sprite):
    def __init__(self, display, scale, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.scale = scale
        self.width = width # where in display piece is started
        self.height = height # where in display piece is started
        self.possible_pieces = ["1", "L", "J", "Z", "S", "T", "R"]
        self.possible_colors = ["orange", (204,204,0), "purple", "blue", "red", (102, 204,0), "brown"]
        self.color_piece = dict(zip(self.possible_pieces, self.possible_colors))
        self.piece = ""
        self.coord = {}

    def choose_piece(self):
        self.piece = random.choice(self.possible_pieces)

    def set_coord(self):
        self.coord = {
            "1": [(self.width, self.height), (self.width, self.height+1), (self.width, self.height+2), (self.width,self.height+3)],
            "L": [(self.width, self.height), (self.width, self.height+1), (self.width, self.height+2), (self.width+1,self.height+2)],
            "J": [(self.width, self.height), (self.width, self.height+1), (self.width, self.height+2), (self.width-1,self.height+2)],    
            "R": [(self.width, self.height), (self.width+1, self.height), (self.width, self.height+1), (self.width+1,self.height+1)],
            "S": [(self.width, self.height), (self.width+1, self.height), (self.width, self.height+1), (self.width-1, self.height+1)],
            "T": [(self.width, self.height), (self.width, self.height+1), (self.width-1, self.height+1), (self.width+1, self.height+1)],
            "Z": [(self.width, self.height), (self.width-1, self.height), (self.width+1, self.height+1), (self.width, self.height+1)]
        }

        
    def set_pos(self, vector):
        x, y = vector
        new_pos = []
        for x_f, y_f in self.coord[self.piece]:
            new_pos.append(((x_f + x), (y_f + y)))    

        self.coord[self.piece] = new_pos

    def set_coord_rotate(self, new_coord):
        self.coord[self.piece] = new_coord
        

    def fill(self):
        for x,y in self.coord[self.piece]:
            self.rect = pygame.Rect(x*self.scale, y*self.scale, self.scale, self.scale)
            pygame.draw.rect(self.display, self.color_piece[self.piece], self.rect)
  