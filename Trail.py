from Body import Body
from geometry import *

class Trail(Body):
    def __init__(self,bird):
        Body.__init__(self, bird.position, -bird.velocity + Vector2D.random(0.5), bird.world)
    def step(self):
        Body.step(self)
        if self.velocity.magnitude() < 0.1:
            self.world.removeBody(self)
    def steer(self):
        return -self.velocity * 0.5
    def color(self):
        if self.velocity.magnitude() > 0.7:
            return "#FF0000"   
        elif self.velocity.magnitude() > 0.55:
            return "#FF9E9E"  
        elif self.velocity.magnitude() > 0.4:
            return "#FFF39E"  
        else:
            return "#DEDEDE"   