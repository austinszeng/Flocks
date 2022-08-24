from Bird import Bird
from geometry import Vector2D

'''
Different color from other birds and ignores other birds.
Moves towards mouse pointer when outside a certain radius of 
the leaders position.
'''
class Leader(Bird):
    def __init__(self, p0, v0, flock, world):
        Bird.__init__(self, p0, v0, flock, world)
        self.RADIUS = 10.0
    def color(self):
        return "#FFFF00"
    # move towards mouse pointer when within a self.RADIUS
    # otherwise, current heading is maintained
    def steer(self):
        accel = Vector2D()
        offset = self.world.pointer() - self.position
        if offset.magnitude() >= self.RADIUS:
            accel = accel + offset
            
        return accel.direction()