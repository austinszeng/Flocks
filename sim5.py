import time
from World import World
from Flock import Flock
from Bird import Bird
from Hawk import Hawk
from geometry import Point2D, Vector2D

#
# CSCI 121: Flocks
# Project 3 Option #2 Exercise 5
#
# This script runs the simulation for EXERCISE 5.
#

# Initialize the world and its window.
world = World(60.0,45.0,800,600,topology='wrapped')
flock = Flock(Bird,25,world)
world.addSystem(flock)
hawk = Hawk(Point2D(0.0,0.0),Vector2D(0.0,0.0),flock,world)
world.addBody(hawk)
flock.registerPredator(hawk)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    world.step()
    world.render()
