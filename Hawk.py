from Bird import Bird
from geometry import Vector2D

class Hawk(Bird):
    def __init__(self, p0, v0, flock, world):
        Bird.__init__(self, p0, v0, flock, world)
        self.flock = None
        self.flock_loc = flock
    def color(self):
        return "#FF0000"
    # accelerate in the direction of the center of the flock
    def steer(self):
        nearby = self.flock_loc.allOnScreen(excluding=[self])

        accel = Vector2D()
        # calculate the center of the flock by using the positions 
        # of all the birds 
        for other in nearby:
            offset = other.position - self.position
            accel = accel + offset

        return accel.direction() 