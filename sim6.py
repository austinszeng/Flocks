import time
from World import World
from Flock import Flock
from Herder import Herder
from Bird import Bird
from geometry import Point2D, Vector2D

#
# CSCI 121: Flocks
# Project 3 Option #2 Exercise 6
#
# This script runs the simulation for EXERCISE 6.
#


# Initialize the world and its window.
world = World(60.0,45.0,800,600,topology='wrapped')
flock = Flock(Bird,16,world)
for _ in range(5):
    h = Herder(Point2D.random(world.bounds),Vector2D(0.0,1.0),flock,world)
    flock.add(h)
world.addSystem(flock)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    world.step()
    world.render()
