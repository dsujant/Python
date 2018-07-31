# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 20:49:19 2018

@author: diana

This program will calculate the area of a circle or triangle.  
User will be prompted to enter a shape and the property of the shape, 
such as length, height, radius

"""
print("Welcome to the Area Calculator!")
option = input("Enter C for Circle or T for Triangle: ")
if option =='C':
    print ("Circle")
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius **2
    print("Area of the circle = " + str(area))
elif option =='T':
    print ("Triangle")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of the triangle = " + str(area))
else:
    print("You entered an invalid shape!")
print("Thank you for using the Area Calculator!")
                           