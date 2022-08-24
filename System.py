#
# System.py
#
# CSCI 121: Flocks
# Project 3 Option #2
#
# This defines the 'System' class which holds a system of moving
# bodies living within a 'World'.
#
# This class is also used as the superclass of 'Flock'.
#

class System:

    def __init__(self, world):
        self.world = world
        self.bodies = []

    # allWithinDistance
    #
    # Returns a list of bodies that are within a certain
    # radius of the given position.
    #
    def allWithinDistance(self, radius, position, excluding=[]):
        bs = []
        for body in self.bodies:
            if body not in excluding and (body.position - position).magnitude() <= radius:
                bs.append(body)
        return bs

    # allOnScreen
    #
    # Returns a list of all bodies that are on the screen
    # for the Hawk class.
    #
    def allOnScreen(self, excluding=[]):
        bs = []
        for body in self.bodies:
            if body not in excluding:
                bs.append(body)
        return bs

    # step
    #
    # Advances the system's simulation by one time step.
    #
    def step(self):

        # Advance each body.
        copy = self.bodies[:]
        for body in copy:
            body.step()


    # add
    #
    # Adds a body to the system.
    #
    def add(self, body):
        self.bodies.append(body)


    # remove
    #
    # Removes a body from the system.
    #
    def remove(self, body):
        self.bodies.remove(body)


    #
    # Quick way to get "for b in sys:" to work.
    #
    def __getitem__(self,i):
        return self.bodies[i]
