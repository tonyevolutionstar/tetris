import pygame
import random 
import math
from pygame.sprite import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, display, scale, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.scale = scale 
        self.width = width
        self.height = height
        self.x =  math.floor(width / 2)
        self.length = 4
        self.pieces_dict = {}
        self.create_pieces()
        self.actual_piece = self.choice_pieces()
        #self.next_p = self.choice_pieces()

        self.rect = self.pieces_dict[self.actual_piece]
        self.color = self.set_color_piece()
        self.rotation = 0 # 0 to 3
     

        
    def create_pieces(self):
         self.pieces_dict = {
            "piece_1": [(self.width,self.height), (self.width,self.height+1), (self.width,self.height+2), (self.width,self.height+3)],
            "piece_l": [(self.width,self.height), (self.width,self.height+1), (self.width,self.height+2), (self.width+1,self.height+2)],
            "piece_j": [(self.width,self.height), (self.width,self.height+1), (self.width,self.height+2), (self.width-1,self.height+2)],    
            "piece_r": [(self.width,self.height), (self.width+1,self.height), (self.width,self.height+1), (self.width+1,self.height+1)],
            "piece_s": [(self.width-1, self.height+1), (self.width, self.height+1), (self.width,self.height), (self.width+1, self.height)],
            "piece_t": [(self.width-1, self.height+1), (self.width, self.height+1), (self.width+1, self.height+1), (self.width,self.height)],
            "piece_z": [(self.width+1, self.height+1), (self.width, self.height+1), (self.width,self.height), (self.width-1, self.height)]
        }
    
    """
    def create_pieces(self):
        self.pieces_dict = {
            "piece_1": [(self.x,1), (self.x,2), (self.x,3), (self.x,4)],
            "piece_l": [(self.x,1), (self.x,2), (self.x,3), (self.x+1,3)],
            "piece_j": [(self.x,1), (self.x,2), (self.x,3), (self.x-1,3)],    
            "piece_r": [(self.x,1), (self.x+1,1), (self.x,2), (self.x+1,2)],
            "piece_s": [(self.x-1, 2), (self.x, 2), (self.x,1), (self.x+1, 1)],
            "piece_t": [(self.x-1, 2), (self.x, 2), (self.x+1, 2), (self.x,1)],
            "piece_z": [(self.x+1, 2), (self.x, 2), (self.x,1), (self.x-1, 1)]
        }s
    """
    


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



    def rotate(self):
        #https://github.com/StanislavPetrovV/Python-Tetris/blob/master/main.py
        
        if self.actual_piece != "piece_r":
            new_l = []
            
            center = self.pieces_dict[self.actual_piece][1] # middle
            x_c, y_c = center  
            for x, y in self.pieces_dict[self.actual_piece]:
                new_x = y - y_c
                new_y = x - x_c
                x = x_c - new_x
                y = y_c + new_y
                new_l.append((x,y))
            self.pieces_dict[self.actual_piece] = new_l 
    