import pygame

class InputHandler:
    count = 1 
  
    """
    state = "soft", "hold" 
    first three are drops, the last is hold the piece
    """    
    def handleInput(self, event, image_ori, state, count): 
        if event.key == pygame.K_c:
            state = "hold"
            self.count = count
            self.count += 1 
            image_ori = (0, 0)
        else:
            image_ori = (0, 0)
        
        return image_ori, state, self.count
