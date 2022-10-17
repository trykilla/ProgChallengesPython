#!/usr/bin/python3

#You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. 
# You are required to print the angle between the plane made by the points A, B, C and B, C, D 
# in degrees(not radians). Let the angle be PHI.
# Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD. Here, X.Y means the dot product of X and Y,
# and AB x BC means the cross product of vectors AB and BC. Also, AB = B - A.

import math

# class Points(object):
#     def __init__(self, x, y, z):

#     def __sub__(self, no):

#     def dot(self, no):

#     def cross(self, no):
        
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    xyz = float(input())