import time
from World import World
from Flock import Flock
from Chaser import Chaser
from Mouse import Mouse

#
# CSCI 121: Flocks
# Project 3 Option #2 Exercise 3
#
# This script runs the simulation for EXERCISE 3.
#

# Initialize the world and its window.
world = World(60.0,45.0,800,600,topology='wrapped')

# Make the flock of chaser birds and place them into the world.
flock = Flock(Chaser,25,world)
world.addSystem(flock)

# Make a mouse body and place it in the world.
mouse = Mouse(world)
world.addBody(mouse)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    world.step()
    world.render()
