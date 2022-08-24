from random import random
from geometry import Point2D, Vector2D
from System import System

EPSILON = 0.000001

#
# Flock.py
#
# CSCI 121: Flocks
# Project 3 Option #2
#

#
# DESCRIPTION:
#
# The code below keeps track of a flock of birds for a bird 
# simulation.  It inherits from class 'System'.
#
#   __init__ : construct a flock of birds of a specified subclass
#   registerLeader: for EXERCISE 4
#   registerPredator: for EXERCISE 5
#
class Flock(System):

    # Flock(cls, size, world):
    #
    # Create a new instance with 'size' new birds, with each being
    # an instance of class 'class'. These all get added to the 
    # world 'world'.
    #
    def __init__(self, cls, size, world):
        System.__init__(self, world)
        self.leader   = None
        self.predator = None
        self.flock_other = None

        # Build the collection of birds.
        # Give each bird a random position and trajectory.
        for i in range(size):
            p0 = Point2D.random(self.world.bounds)
            v0 = Vector2D.random(cls.MAXIMUM_SPEED)
            # The provided class 'cls' better have a bird-like __init__.
            b = cls(p0, v0, self, self.world)
            self.add(b)

    def registerPredator(self, predator):
        self.predator = predator

    def registerLeader(self, leader):
        self.leader = leader

    def registerFlockOther(self, flock_other):
        self.flock_other = flock_other

    
