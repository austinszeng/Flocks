from Body import Body
from geometry import Vector2D

class Mouse(Body):
    def __init__(self, world):
        super().__init__(world.pointer(), Vector2D(), world)
    def step(self):
        self.position = self.world.pointer()
    def color(self):
        return "#FFFF00"