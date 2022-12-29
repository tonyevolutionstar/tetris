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
        self.possible_colors = ["orange", "yellow", "purple", "blue", "red", "green", "brown"]
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

    def rotate(self):
        #https://github.com/StanislavPetrovV/Python-Tetris/blob/master/main.py
        
        if self.piece != "R":
            new_l = []
            center = self.coord[self.piece][3] # middle
            x_c, y_c = center  
            for x, y in self.coord[self.piece]:
                new_x = y - y_c
                new_y = x - x_c
                x = x_c - new_x
                y = y_c + new_y
                new_l.append((x,y))
            self.coord[self.piece] = new_l 
        else:

            return 0
        return 1


    def fill(self):
        for x,y in self.coord[self.piece]:
            self.rect = pygame.Rect(x*self.scale, y*self.scale, self.scale, self.scale)
            pygame.draw.rect(self.display, self.color_piece[self.piece], self.rect)
    

    