import time
from World import World
from Flock import Flock
from Bird import Bird
from Shark import Shark
from Jet import Jet
from geometry import Point2D, Vector2D

#
# CSCI 121: Flocks
# Project 3 Option #2 Exercise 7
#
# This script runs the simulation for EXERCISE 7 (Sharks and Jets).
#


# Initialize the world and its window.
world = World(60.0,45.0,800,600,topology='wrapped')
# Initialize flocks with no birds in them
flock = Flock(Bird, 0, world)
flock2 = Flock(Bird, 0, world)
# Add sharks to flock and have flock2 be flock_other
for _ in range(8):
    shark = Shark(Point2D.random(world.bounds),Vector2D(0.0,1.0),flock,world,flock2)
    flock.add(shark)
# Add jets to flock2 and have flock be flock_other
for _ in range(8):
    jet = Jet(Point2D.random(world.bounds),Vector2D(0.0,1.0),flock2,world,flock)
    flock2.add(jet)
world.addSystem(flock)
world.addSystem(flock2)
flock.registerFlockOther(flock2)
flock2.registerFlockOther(flock)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    world.step()
    world.render()
