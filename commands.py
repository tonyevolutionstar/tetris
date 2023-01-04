import pygame 

class Command:   
    def execute():
        raise NotImplementedError


class Up(Command):
    def execute(self, actor, new_coord):
        actor.set_coord_rotate(new_coord)

class Down(Command):
    def execute(self, actor, vector):
        actor.set_pos(vector)
        
class Left(Command):
    def execute(self, actor, vector):
        actor.set_pos(vector)

class Right(Command):
    def execute(self, actor, vector):
        actor.set_pos(vector)

class Z(Command):
    def execute(self, actor, new_coord):
        actor.set_coord_rotate(new_coord)


class InputHandler:
    command = {
        pygame.K_LEFT: Left,
        pygame.K_DOWN: Down,
        pygame.K_RIGHT: Right,
        pygame.K_UP: Up,
        pygame.K_z: Z
    }

    def handleInput(self, event, actor, vector):
        self.command[event].execute(self, actor, vector)
