import time
from World import World
from Flock import Flock
from Leader import Leader
from Follower import Follower
from geometry import Point2D,Vector2D

#
# CSCI 121: Flocks
# Project 3 Option #2 Exercise 4
#
# This script runs the simulation for EXERCISE 4.
#

# Initialize the world and its window.
world = World(60.0,45.0,800,600,topology='wrapped')

# Make the flock of follower birds and then add a leader.
flock = Flock(Follower,25,world)
leader = Leader(Point2D(0.0,0.0),Vector2D(1.0,0.0),flock,world)
flock.add(leader)
flock.registerLeader(leader)

# Place all the flock's birds into the world.
world.addSystem(flock)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    world.step()
    world.render()
