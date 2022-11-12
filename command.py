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
    state = "normal", "hard", "soft", "hold" 
    first three are drops, the last is hold the piece
    """    
    def handleInput(self, event, image_ori, state):
        print(event.key)
        if event.key == pygame.K_z:
            image_ori = (0, -1)
        elif event.key == pygame.K_UP:
            image_ori = (0, 1)
        elif event.key == pygame.K_LEFT:
            image_ori = (-1, 0)
        elif event.key == pygame.K_RIGHT:
            image_ori = (1, 0)
        elif event.key == pygame.K_c:
            state = "hold"
        elif event.key == pygame.K_DOWN:
            state = "soft"
        elif event.key == pygame.K_SPACE:
            state = "hard"
        
        return image_ori, state
