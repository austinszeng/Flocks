from geometry import Vector2D

#
# Body.py
#
# CSCI 121: Flocks
# Project 3 Option #2
#
# This defines the 'Body' class, which all the simulation objects
# inherit from. These objects are minimal---they have no motivation,
# and don't move (have no velocity). 
#

class Body:

    TIME_STEP = 0.5      # I played with this until things looked good.
    MAXIMUM_SPEED = None

    def __init__(self, p0, v0, world):
        self.position0 = p0
        self.velocity0 = v0
        self.world = world
        self.reset()


    def reset(self):
        self.position = self.position0
        self.velocity = self.velocity0
        self.accel = Vector2D()


    def steer(self):
        # By default, bodies don't move.  Return the 0 vector.
        return Vector2D()


    def color(self):
        # Blue is our generic color.  Let's us know that
        # we forgot to override the color.
        return "#000080"    # BLUE red:green:blue hex color code


    def shape(self):
        # A little square is our generic shape.
        p1 = self.position + Vector2D( 0.125, 0.125)       
        p2 = self.position + Vector2D(-0.125, 0.125)        
        p3 = self.position + Vector2D(-0.125,-0.125)        
        p4 = self.position + Vector2D( 0.125,-0.125)
        return [p1,p2,p3,p4]


    def rendering(self):
        # A body's rendering can be made up of a colored shapes.
        # The default is just a single color/shape.
        return [(self.color(),self.shape())]


    # step
    #
    # This computes the boid's physical parameters in the next time step.
    #
    def step(self):

        # Update the position, but respect world boundary conditions.
        #
        self.position = self.position + self.velocity * self.TIME_STEP
        self.trimPosition()
    
        # Update the velocity, but limit it if the class does.
        #
        self.velocity = self.velocity + self.accel * self.TIME_STEP
        if self.MAXIMUM_SPEED is not None and self.velocity.magnitude() > self.MAXIMUM_SPEED: 
            self.velocity = self.velocity.direction() * self.MAXIMUM_SPEED 

        # Determine direction boid would like to head, used for the next time step.
        #
        self.accel = self.steer()
    

    def trimPosition(self):
        # By default, make sure the coordinates of the position 
        # of the body respect the world's topology.
        self.world.trim(self)
