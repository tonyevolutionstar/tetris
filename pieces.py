import os
import pygame
from pygame.sprite import *

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.path = os.getcwd() + "\\sprite_sheet\\"
        self.pieces = []
       
        #self.images = self.load_pieces()
        self.image = pygame.image.load(os.path.join(self.path, "1.jpg")).convert()
        self.image = pygame.transform.scale(self.image, (200, 200)) 
        self.rect = Rect(50, 100, 300, 200)

        #for img in self.images:
        #    self.image = self.images[img]

    def load_pieces(self):
        filenames = [f for f in os.listdir(self.path) if f.endswith('.jpg')]
        images = {}
        for name in filenames:
            imagename = os.path.splitext(name)[0] 
            images[imagename] = pygame.image.load(os.path.join(self.path, name)).convert_alpha()
        return images 