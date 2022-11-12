import os
import pygame
import random 
from pygame.sprite import *

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.path = os.getcwd() + "\\sprite_sheet\\"
        pieces_choosed = self.choice_pieces()
        self.image = pygame.image.load(pieces_choosed).convert()
        self.image = pygame.transform.scale(self.image, (34, 75)) 
        self.rect = Rect(140, 60, 300, 100)

    def next_piece(self):
        self.path = os.getcwd() + "\\sprite_sheet\\"
        pieces_choosed = self.choice_pieces()
        self.image = pygame.image.load(pieces_choosed).convert()
        self.image = pygame.transform.scale(self.image, (20, 44)) 
        self.rect = Rect(320, 120, 20, 50)
        

    def choice_pieces(self):
        pieces_list = ['1.png', 'L.png', 'R.png', 'S.png', 'T.png']
        return self.path + random.choice(pieces_list)

class Background(pygame.sprite.Sprite):
    def __init__(self, SCALE, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "\\sprite_sheet\\"+'background.jpg').convert()
        self.image = pygame.transform.scale(self.image, (SCALE * WIDTH, SCALE * HEIGHT)) 
        self.rect = Rect(0, 0, SCALE * WIDTH, SCALE * HEIGHT)