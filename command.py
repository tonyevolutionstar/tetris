import pygame


class InputHandler:

    def __init__(self, pieces_pos, x_left, x_right, limit_y):
        self.pieces_pos = pieces_pos
        self.x_left = x_left
        self.x_right = x_right
        self.limit_y = limit_y
        self.play = 1
        #self.screen_limit()

    def screen_limit(self):
        
        x_first, y_first = self.pieces_pos[0]
        print(x_first, y_first)
        print(self.x_left)

        if (x_first == self.x_left or x_first == self.x_right):
            self.play = 0
        elif (y_first > self.limit_y):
            self.play = 0


    """
    state = "hard", "soft", "hold" 
    first three are drops, the last is hold the piece
    """    
    def handleInput(self, event, image_ori, state):
        
        #print(self.play)
    
        if event.key == pygame.K_z:
            pass # rotate left
        elif event.key == pygame.K_UP:
            pass # rotate right
        elif event.key == pygame.K_LEFT and self.play == 1:
            image_ori = (-1, 0)
        elif event.key == pygame.K_RIGHT:
            image_ori = (1, 0)
        elif event.key == pygame.K_c:
            state = "hold"
        elif event.key == pygame.K_DOWN:
            state = "soft"
            image_ori = (0, 1)
        elif event.key == pygame.K_SPACE:
            state = "hard"
            image_ori = (0, 1)
        

        return image_ori, state
