from tkinter import *
from System import System
from geometry import Bounds, Point2D

#
# World.py
#
# CSCI 121: The Boids
# Project 3 Option #2
#
# This defines the 'world' class, an object that tracks two things for
# the flock simulator:
#
#   * The world of simulated bodies that inhabit the system.
#   * The graphical window that depicts those bodies.
#
# A 'World' has a coordinate system, one that's specified with a
# certain width and a certain height, and whose origin normally sits
# in the center. Bodies that inhabit this world live at points within
# this coordinate system. A world drives the simulation of these
# bodies, and also draws them in its window. The key methods for
# managing the simulation are:
#  
#   addBody: adds a Body object to the system to be simulated
#   addSystem: adds a collection of bodies to the system
#   removeBody: removes a Body object from the simulated system
#   step: advances the simulation by one time step
# 
# Here are the key methods used by the system to draw the contents
# of the simulation:
#
#   render: clears then draws all the bodies' shapes into the window 
#   drawShape: used by 'render' to depict a body. Uses each body's
#      'color' and 'shape' attributes to draw them.
#
# These rely on the underlying tkinter.Frame class from which this
# class inherits. There is also some minimal support for
# interaction---the method 'pointer' (using 'windowCoordToWorld' 
# allows you to ask the world object where the mouse pointer
# sits.
#

class World(Frame):

    # World(n,w,h,ww,wh)
    #
    # Creates a world with a coordinate system of width w and height
    # h, with x coordinates ranging between -w/2 and w/2, and with y
    # coordinates ranging between -h/2 and h/2.
    # 
    # Creates a corresponding graphics window, for rendering 
    # the world, with pixel width ww and pixel height wh.
    #
    def __init__(self, w, h, ww, wh, topology = 'wrapped'):

        # Register the world coordinate and graphics parameters.
        self.WINDOW_WIDTH = ww
        self.WINDOW_HEIGHT = wh
        self.bounds = Bounds(-w/2,-h/2,w/2,h/2)
        self.topology = topology

        # Populate the world with creatures
        self.bodies = System(self)

        # Initialize the graphics window.
        self.root = Tk()
        self.root.title('MATH 121 Bird Simulation')
        Frame.__init__(self, self.root)
        self.canvas = Canvas(self.root, 
                             width=self.WINDOW_WIDTH,
                             height=self.WINDOW_HEIGHT)

        # Handle mouse pointer motion events.
        self.mouse_location = Point2D()
        def motion(event):
            self.mouse_location = self.windowCoordToWorld(event.x,event.y)
        self.canvas.bind('<Motion>',motion)

        # Finalize the creation of the windowed display.
        self.canvas.pack()
        self.pack()
        self.render()


    # trim
    #
    # Modify the coordinates of a body so that they respect the
    # topology.
    #
    def trim(self,body):
        if self.topology == 'wrapped':
            body.position = self.bounds.wrap(body.position)
        elif self.topology == 'bound':
            body.position = self.bounds.clip(body.position)
        elif self.topology == 'open':
            pass

    # step
    #
    # Advance the simulation one animation frame.
    #
    def step(self):
        self.bodies.step()

    # addBody
    #
    # Puts another body into the world's system.
    #
    def addBody(self, bdy):
        self.bodies.add(bdy)


    # removeBody
    #
    # Removes a body from the world's system.
    #
    def removeBody(self, bdy):
        self.bodies.remove(bdy)


    # addSystem
    #
    # Adds a system of bodies into the world's system.
    #
    def addSystem(self, system):
        for body in system:
            self.addBody(body)
               
    # render
    #
    # This redraws the world's contents.
    #
    def render(self):
        self.clear()
        for body in self.bodies:
            parts = body.rendering()
            for part in parts:
                color = part[0]
                shape = part[1]
                self.drawShape(shape,color)
        self.update()

    # drawShape
    #
    # Renders a polygonal shape, specified as a list of Point2d objects 
    # in world coordinates, within the world window at the specified color.
    #
    def drawShape(self, shape, color):

        wh = self.WINDOW_HEIGHT
        h = self.bounds.height()
        ww = self.WINDOW_WIDTH
        x = self.bounds.xmin
        y = self.bounds.ymin

        # Scale the object's coordinates so that the origin sits at the
        # center of the window, and so that the objects are rescaled to
        # the width and height of the window.
        pairs = [ ((p.x - x)*wh/h, wh - (p.y - y)* wh/h) for p in shape ]
        pairs.append(pairs[0])
        self.canvas.create_polygon(pairs, fill=color)

    # clear
    #
    # Erases the contents of the window to prepare drawing the next frame.
    #
    def clear(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, 
                                     self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                     fill="#000000")

    # windowCoordToWorld
    #
    # Converts a location within the graphics window into a point
    # with coordinates of the world's system. (Used for querying
    # the mouse pointer's location.)
    #
    def windowCoordToWorld(self,x,y):
        return self.bounds.pointAt(x/self.WINDOW_WIDTH,
                                    1.0-y/self.WINDOW_HEIGHT)


    # pointer:
    #
    # Used by code to find out where the mouse pointer is sitting.  It
    # gives back a Point2D object with world coordinates corresponding
    # to the location where the mouse pointer sits in the graphics
    # window.
    #
    def pointer(self):
        return self.mouse_location.copy()
