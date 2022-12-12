import pygame
import random 
import math
from pygame.sprite import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, display, scale, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.scale = scale 
        self.x =  math.floor(width / 2)
        self.length = 4
        self.pieces_dict = {}
        self.create_pieces()
        self.actual_piece = self.choice_pieces()
        #self.actual_piece = "piece_z"
        self.rect = self.pieces_dict[self.actual_piece]
        self.color = self.set_color_piece()
        

    def create_pieces(self):
        self.pieces_dict = {
            "piece_1": [(self.x,1), (self.x,2), (self.x,3), (self.x,4)],
            "piece_l": [(self.x,1), (self.x,2), (self.x,3), (self.x+1,3)],
            "piece_j": [(self.x,1), (self.x,2), (self.x,3), (self.x-1,3)],    
            "piece_r": [(self.x,1), (self.x+1,1), (self.x,2), (self.x+1,2)],
            "piece_s": [(self.x-1, 2), (self.x, 2), (self.x,1), (self.x+1, 1)],
            "piece_t": [(self.x-1, 2), (self.x, 2), (self.x+1, 2), (self.x,1)],
            "piece_z": [(self.x+1, 2), (self.x, 2), (self.x,1), (self.x-1, 1)]
        }


    def choice_pieces(self):
        pieces_choosed = ""
        random_piece = random.choice(list(self.pieces_dict.values()))
        
        for piece in self.pieces_dict:
            if self.pieces_dict[piece] == random_piece:
                pieces_choosed = piece

        return pieces_choosed


    def set_color_piece(self):
        colors = { "piece_1": "orange", "piece_l": "yellow", "piece_j":"purple", "piece_r": "brown", 
                "piece_s": "red", "piece_z": "blue", "piece_t": "green"}

        self.color = colors[self.actual_piece]

        return self.color


    def fill_piece(self):
        for x,y in self.pieces_dict[self.actual_piece]:
            self.rect = pygame.Rect(self.scale * x, self.scale * y, self.scale, self.scale)
            pygame.draw.rect(self.display, self.color, (self.scale * x, self.scale * y, self.scale, self.scale))
                   

    def change_dir(self, vector):
        new_list = []
        x, y = vector
    
        for x_p, y_p in self.pieces_dict[self.actual_piece]:
            
            new_list.append((x_p + x, y_p + y))
        self.pieces_dict[self.actual_piece] = new_list

