from Body import Body
from geometry import Vector2D
from Trail import Trail # EXERCISE 1 and 2

#
# Bird.py
#
# CSCI 121: Flocks
# Project 3 Option #2
#
# This defines the 'Bird' class, a simulated body that moves in a
# world according to its behavior, determined by its own motivations
# and the presence of other birds it reacts to.
#
# Below are the modifications we suggest for each of the exercises.
#

# EXERCISE 1
#
# . add a 'leave_trail' attribute that is either True/False
# . add a 'def setTrail(b)' method where 'b' is either True/False, for
#     turning on/off a bird's trail-leaving feature
# . modify 'step' to create a Trail object at a bird's position, but
#     only when it should be leaving a trail

# EXERCISE 2
#
# . modify 'step' to create three Trail objects at a bird's position, but
#     only when it should be leaving a trail

# EXERCISE 5
#
# . create a FLEE_COEFF (and perhaps a FLEE_RADIUS)
# . make computeFlee method that computes the acceleration component
#     when there's a predator nearby (according to FLEE_RADIUS)
# . change steer method to computeFlee using FLEE_COEFF
# . set the 'worried' attribute to True when it sees a predator, 
#     otherwise have that attribute be False  
#

EPSILON = 0.000001

#
# class Bird
#
# Implements one of the flocking agents, one of Reynolds' "boids".
# A bird has a velocity and a position.  These get updated over
# time using first-order Euler integration.  This is handled in
# the method 'step', which relies on the Point2D and Vector2D
# methods to modify a bird's position according to its velocity.
#
class Bird(Body):

    AVOID_RADIUS = 5.0
    MIMIC_RADIUS = 10.0
    COHERE_RADIUS = 20.0
    FLEE_RADIUS = 21.6
    TRIBAL_RADIUS = 12.0

    AVOID_COEFF = 10.0
    MIMIC_COEFF = 10.0
    COHERE_COEFF = 5.0
    FLEE_COEFF = 11.0
    TRIBAL_COEFF = 11.0

    MAXIMUM_SPEED = 1.0

    def __init__(self, p0, v0, flock, world, flock_other=None):
        Body.__init__(self, p0, v0, world)
        self.flock = flock
        self.flock_other = flock_other
        self.worried = False
        self.leave_trail = True


    def setTrail(self,b):
        self.leave_trail = b


    def color(self):
        # These birds are white, unless they are flustered.
        if self.worried:
            return "#FF8080"   # PINK red:green:blue hex code
        else:
            return "#FFFFFF"   # WHITE red:green:blue hex code


    def shape(self):
        h = self.velocity.direction()
        hp = h.perp()
        p1 = self.position + h
        p2 = self.position + hp * 0.5
        p3 = self.position - hp * 0.5
        return [p1,p2,p3]


    def computeCohere(self):

        nearby = self.flock.allWithinDistance(self.COHERE_RADIUS, self.position, excluding=[self])

        # Try to be around other birds.
        cohere  = Vector2D()
        for other in nearby:
            offset = other.position - self.position
            cohere = cohere + offset

        # We'll normalize the cohere vector.  If we don't, birds will
        # work harder if they are further away from the center of the
        # group.  That's a nice effect, too, but it often creates
        # instabilities in the activity of the simulation.
        return cohere.direction()


    def computeMimic(self):

        nearby = self.flock.allWithinDistance(self.MIMIC_RADIUS, self.position, excluding=[self])

        # Try to mimic the heading of nearby birds.
        align = Vector2D()
        for other in nearby:
            align = align + other.velocity

        # Return a normalized align vector (see note for 'cohere' above).
        return align.direction()


    def computeAvoid(self):

        nearby = self.flock.allWithinDistance(self.AVOID_RADIUS, self.position, excluding=[self])

        # Try to avoid nearby birds.
        separate = Vector2D()
        for bird in nearby:
            offset = bird.position - self.position
            distance = offset.magnitude()
            if distance > EPSILON:
                # Head away from this other bird, with a 
                # strength proportional to 1/d^2.  Closer
                # birds should be avoided more furiously.
                away = -offset
                weight = 1.0 / distance * distance
                separate = separate + away * weight

        # Return a normalized separate vector (see note for 'cohere' above).
        return separate.direction()


    def computeFlee(self):
        #
        # Exercise 5
        #
        flee = Vector2D()
        if self.flock.predator is not None:
            # Try to avoid predators
            if (self.flock.predator.position - self.position).magnitude() <= self.FLEE_RADIUS:
                self.worried = True
                offset = self.position - self.flock.predator.position
                flee = flee + offset
            else:
                self.worried = False
        
        return flee.direction()

    def computeTribal(self):
        #
        # Sharks and Jets 
        #
        separate = Vector2D()
        if self.flock.flock_other is not None:
            # Try to avoid other flock
            nearby = self.flock_other.allWithinDistance(self.TRIBAL_RADIUS, self.position, excluding=[self])

            for bird in nearby:
                offset = self.position - bird.position
                separate = separate + offset
        # Return a normalized separate vector (see note for 'cohere' above).
        return separate.direction()

    #
    # steer and/or apply thrust
    #
    # Figure out the acceleration direction of one bird
    # by having it compare itself to the others.
    #
    def steer(self):

        # Compute the directions of three competing concerns.
        repel = self.computeAvoid()
        align = self.computeMimic()
        group = self.computeCohere()
        run = self.computeFlee()
        avoid = self.computeTribal()
        
        # Compute a weighted average of these concerns' directions.
        accel = Vector2D()
        accel = accel + repel.direction() * self.AVOID_COEFF
        accel = accel + align.direction() * self.MIMIC_COEFF
        accel = accel + group.direction() * self.COHERE_COEFF
        accel = accel + run.direction() * self.FLEE_COEFF
        accel = accel + avoid.direction() * self.TRIBAL_COEFF

        # only include flee/tribal in the weighted average when there is a predator/other flock
        # if included when they don't exist, other concerns are not shown as well
        if self.flock.predator == None and self.flock.flock_other == None:
            total_weight = self.AVOID_COEFF + self.MIMIC_COEFF + self.COHERE_COEFF 
        elif self.flock.predator != None and self.flock.flock_other == None:
            total_weight = self.AVOID_COEFF + self.MIMIC_COEFF + self.COHERE_COEFF + self.FLEE_COEFF
        elif self.flock.predator == None and self.flock.flock_other != None:
            total_weight = self.AVOID_COEFF + self.MIMIC_COEFF + self.COHERE_COEFF + self.TRIBAL_COEFF
        else:
            total_weight = self.AVOID_COEFF + self.MIMIC_COEFF + self.COHERE_COEFF + self.FLEE_COEFF + self.TRIBAL_COEFF
        return accel.over(total_weight)


    #
    # step
    #
    # Change position, etc with a time step.
    # 
    def step(self):
        # Just use the superclass step method, but enhance for some exercises.
        Body.step(self)
        t0 = Trail(self)
        t1 = Trail(self)
        t2 = Trail(self)
        self.world.addBody(t0)
        self.world.addBody(t1)
        self.world.addBody(t2)



        # EXERCISE 2 and 3 work goes here.

    # __str__
    #
    # Gives a bird report, decribing its position.
    #
    def __str__(self):
        return "bird "+Body.__str__(self)+" at "+str(self.position)

