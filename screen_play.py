import pygame 

class Screen_play(pygame.sprite.Sprite):
    def __init__(self, display, x_l, x_r, top, bottom, scale):
        pygame.sprite.Sprite.__init__(self)
        self.x_l = x_l
        self.x_r = x_r
        self.top = top
        self.bottom = bottom
        self.display = display
        self.scale = scale
        self.grid = {}
        self.free_pos = []

    def create_grid(self):
        for x in range(self.x_l, self.x_r, self.scale):
            for y in range(self.top, self.bottom, self.scale):
                self.grid[int(x/10), int(y/10)] = "white"
               
        return self.grid


    def set_grid(self, pos, color):
        for val_pos in pos:  
            self.grid[val_pos] = color


    def draw_grid(self):
        for x in range(self.x_l, self.x_r, self.scale):
            for y in range(self.top, self.bottom, self.scale):
                self.rect = pygame.Rect(x, y, self.scale, self.scale)
                pygame.draw.rect(self.display, (223, 223, 223), self.rect, 1)


    def fill(self):
        for val in self.grid:
            x, y = val
            self.rect = pygame.Rect(x * self.scale, y * self.scale, self.scale, self.scale)
            pygame.draw.rect(self.display, self.grid[(x,y)], self.rect)

    
        