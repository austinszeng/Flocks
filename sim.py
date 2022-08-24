import time
from World import World
from Flock import Flock
from Bird import Bird

#
# CSCI 121: The Boids
# Project 3 Option #2
#
# This script runs a basic simulation to demonstrate the project.
# You'll mimic this script, write your own copy, for each of the
# exercises you choose to complete. (See sim1.py, sim2.py, etc.
# in this same folder for examples for their exercises.)
#

# Initialize the world and its window.
world = World(60.0, 45.0, 800, 600, topology='wrapped')
flock = Flock(Bird, 25, world)
world.addSystem(flock)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    world.step()
    world.render()
