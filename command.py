import pygame

class Command: 
    def execute(self):
        raise NotImplemented

class RotateRight(Command):#z
    def execute(self, actor):
        actor.rotateright()

class RotateLeft(Command): #arrow up
    def execute(self, actor):
        actor.rotateleft()

class MoveRight(Command): #arrow right
    def execute(self, actor):
        actor.moveright()

class MoveLeft(Command): #arrow left
    def execute(self, actor):
        actor.moveleft()        

class HardDrop(Command): #space
    def execute(self, actor):
        actor.harddrop()

class SoftDrop(Command):  #arrow down
    def execute(self, actor):
        actor.softdrop()

class Hold(Command): #c
    def execute(self, actor):
        actor.hold()

class InputHandler:
    command = {
        "z": RotateLeft,
        "c": Hold,
        "K_UP": RotateRight,
        "K_DOWN": SoftDrop,
        "K_LEFT": MoveLeft,
        "K_RIGHT": MoveRight,
        "K_SPACE": HardDrop
    }

    """
    state = "hard", "soft", "hold" 
    first three are drops, the last is hold the piece
    """    
    def handleInput(self, event, image_ori, state, wall):
        
        if event.key == pygame.K_LEFT and wall == 1:
            image_ori = (1, 0)
        elif  event.key == pygame.K_RIGHT and wall == 1:
            image_ori = (-1, 0)
        elif event.key == pygame.K_DOWN and wall == 1:
            image_ori = (0, -1)


        if event.key == pygame.K_z:
            pass # rotate left
        elif event.key == pygame.K_UP:
            pass # rotate right
        elif event.key == pygame.K_LEFT and wall == 0:
            image_ori = (-1, 0)
        elif event.key == pygame.K_RIGHT and wall == 0:
            image_ori = (1, 0)
        elif event.key == pygame.K_c:
            state = "hold"
        elif event.key == pygame.K_DOWN and wall == 0:
            state = "soft"
            image_ori = (0, 1)
        elif event.key == pygame.K_SPACE and wall == 0:
            state = "hard"
            image_ori = (0, 1)
      

        return image_ori, state
