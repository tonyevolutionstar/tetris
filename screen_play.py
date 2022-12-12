import pygame 

class Screen_play(pygame.sprite.Sprite):
    def __init__(self, display, x, y, width, height, SCALE):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect =  pygame.Rect(x, y, width * SCALE, height * SCALE)
        self.display = display
        
    def draw_screen(self):
        pygame.draw.rect(self.display, (0,0,0), self.rect, 2)
