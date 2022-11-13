from msilib.schema import Class
import pygame
import random 
import math
from pygame.sprite import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, display, scale, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.scale = scale 

        x =  math.floor(width / 2)

        self.pieces_dict = {}
        self.pieces_dict["piece_1"] = [(x,1), (x,2), (x,3), (x,4)]
        self.pieces_dict["piece_l"] = [(x,1), (x,2), (x,3), (x+1,3)]
        self.pieces_dict["piece_r"] = [(x,1), (x+1,1), (x,2), (x+1,2)]
        self.pieces_dict["piece_s"] = [(x-1, 2), (x, 2), (x,1), (x+1, 1)]
        self.pieces_dict["piece_t"] = [(x-1, 2), (x, 2), (x+1, 2), (x,1)]
        self.actual_piece = self.choice_pieces()
        self.color = self.set_color_piece()


    def choice_pieces(self):
        pieces_choosed = ""
        random_piece = random.choice(list(self.pieces_dict.values()))
        
        for piece in self.pieces_dict:
            if self.pieces_dict[piece] == random_piece:
                pieces_choosed = piece

        return pieces_choosed


    def set_color_piece(self):
        if self.actual_piece == "piece_1":
            self.color = "orange"
        elif self.actual_piece == "piece_l":
            self.color = "yellow"
        elif self.actual_piece == "piece_r":
            self.color = "brown"
        elif self.actual_piece == "piece_s":
            self.color = "red"
        elif self.actual_piece == "piece_t":
            self.color = "green"
        return self.color


    def fill_piece(self):
        for piece in self.pieces_dict:
            if piece == self.actual_piece:
                for x,y in self.pieces_dict[piece]:
                    pygame.draw.rect(self.display, self.color, (self.scale * x, self.scale * y, self.scale, self.scale))


class Game_window(pygame.sprite.Sprite):
    def __init__(self, display, x, y, scale):
        
        pygame.sprite.Sprite.__init__(self)
        pygame.draw.rect(display, (0,0,0), (x * scale, y * scale, scale, scale), 2)

