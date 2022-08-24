from Bird import Bird
from geometry import Vector2D

class Chaser(Bird):
    def computeCohere(self):

        # Try to be around pointer.
        cohere  = Vector2D()
        offset = self.world.pointer() - self.position
        cohere = cohere + offset

        return cohere.direction()