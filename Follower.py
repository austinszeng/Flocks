from Bird import Bird
from geometry import Vector2D

class Follower(Bird):
    def computeCohere(self):

        nearby = self.flock.allWithinDistance(self.COHERE_RADIUS, self.position, excluding=[self])
        leader = self.flock.leader

        # Try to be around other birds.
        cohere  = Vector2D()
        if leader == None:
            for other in nearby:
                offset = other.position - self.position
                cohere = cohere + offset
        # If leader exists, move in its direction
        else:
            offset = leader.position - self.position
            cohere = cohere + offset

        return cohere.direction()