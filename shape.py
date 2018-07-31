# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 11:19:30 2018

@author: diana
"""

#Write a classes Cube, Sphere, Cone, and Cylinder, all inherited from a common Shape base class.
#Define methods calculate_volume, calculate_surface_area, set_color, and get_color. 
#Which methods should be implemented in the base class and which should be implemented in the child classes?

from math import pi
class Shape(object):
    
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def get_shape(self):
        return self.shape
    
    def __repr__(self):
        return "Shape: {}, Color: {}".format(self.shape, self.color)


class Cube(Shape):
    
    def __init__(self, shape, color, x):
        Shape.__init__(self, shape, color)
        self.x = x

    def calculate_surface_area(self):
        return 6 * self.x**2
    
    def calculate_volume(self):
        return self.x**3    
    
    
c= Cube('Cube', 'Red', 4)
print c
print 'Cube surface area= ' + str(c.calculate_surface_area())
print 'Cube Volume = ' + str(c.calculate_volume())

#import math
class Sphere(Shape):
    
    def __init__(self, shape, color, x):
        Shape.__init__(self, shape, color)
        self.x = x

    def calculate_surface_area(self):
        return 4 * math.pi * self.x**2
    
    def calculate_volume(self):
        return (4/3 * math.pi * self.x**3)

s= Sphere('Sphere', 'Blue', 3)
print s
print 'Sphere surface area = ' + str(s.calculate_surface_area())
print 'Sphere volume = ' + str(s.calculate_volume())

#import math
class Cone(Shape):
    
    def __init__(self, shape, color, x, h):
        Shape.__init__(self, shape, color)
        self.x = x
        self.h = h

    def calculate_surface_area(self):
        return 4 * math.pi * self.x**2
    
    def calculate_volume(self, h):
        return math.pi * self.x**2 * h/3

    

cone = Cone('Cone', 'Green', 5, 2)
print 'Cone surface area = ' + str(cone.calculate_surface_area())
print 'Cone volume = ' + str(cone.calculate_volume(2))  
    