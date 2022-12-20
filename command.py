import pygame


class InputHandler:
    count = 1 
    """
    state = "hard", "soft", "hold" 
    first three are drops, the last is hold the piece
    """    
    def handleInput(self, event, image_ori, state, count, score_tetris):
       # for hold 
        if event.key == pygame.K_z:

            pass # rotate left
        elif event.key == pygame.K_UP: # rotate right

            image_ori = (0, 1)
        elif event.key == pygame.K_LEFT :
            image_ori = (-1, 0)
        elif event.key == pygame.K_RIGHT:
            image_ori = (1, 0)
        elif event.key == pygame.K_c:
            state = "hold"
            self.count = count
            self.count += 1 
            image_ori = (0, 0)
        elif event.key == pygame.K_DOWN:
            state = "soft"
            image_ori = (0, 1)
            score_tetris += 1
        elif event.key == pygame.K_SPACE:
            state = "hard"
            image_ori = (0, 1)
        else:
            image_ori = (0, 0)
        
        print(state)
        return image_ori, state, self.count, score_tetris
