import pygame


class InputHandler:

    """
    state = "hard", "soft", "hold" 
    first three are drops, the last is hold the piece
    """    
    def handleInput(self, event, image_ori, state):
        if event.key == pygame.K_z:
            pass # rotate left
        elif event.key == pygame.K_UP:
            pass # rotate right
        elif event.key == pygame.K_LEFT :
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
