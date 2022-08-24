from Bird import Bird
from geometry import Vector2D
'''
- act independently; no urge to cohere with flock members. instead, head around them

- if it sees a flock of birds in its view forward in a certain distance away,
    it should choose a heading that steers it to the heading furthest to the right 
    of those birds

1. Scan whole flock but only pay attention to ones that 
    - are not itself
    - are within a certain radius of it
    - are in front of it, but not behind it
2. Among those, pick the rightmost bird 
'''
class Herder(Bird):
    def __init__(self, p0, v0, flock, world):
        Bird.__init__(self, p0, v0, flock, world)
        self.RADIUS = 35.0
    def color(self):
        return "#800080"
    def steer(self):
        nearby = self.flock.allWithinDistance(self.RADIUS, self.position, excluding=[self])

        accel = Vector2D()
        rightmost = None
        for other in nearby:
            hb = other.position - self.position # vector heading from herder to bird
            # if in front of herder
            if self.velocity.dot(hb) > 0.0:
                # pick rightmost bird
                if rightmost == None or hb.cross(rightmost.position - self.position) > 0.0:
                    rightmost = other

        if rightmost != None:
            offset = rightmost.position - self.position
            accel = accel + offset
        
        self.velocity *= 2.0 # make herders faster
        return accel.direction() 