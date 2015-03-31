#! needed libraries 
from __future__ import division
import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv

def alltours_tsp(cities):
    '''Generate all possible tours of the cities and choose
       the shortest tour.
    '''
    return shortest_tour(alltours(cities))

def shortest_tour(tours):
    '''Choose the tour with the minimum tour length.'''
    return min(tours, key = tour_length)



# There is where 'alltours' the fancy comes up
alltours = itertools.permutations


def tour_length(tour):
    '''
    The total of distance between each pair of consecutive cities in the tour
    '''
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))

# Cities are represented as Points, which are represented as complex numbers
Point = complex
City = Point

def X(point):
    '''
    The x coordinate of a point.'''
    return point.real

def Y(point):
    '''
    The y coordinate of a point.'''
    return point.imag

def distance(A, B):
    '''
    The distance between two points.'''
    return abs(A-B)

def Cities(n, width=900, height=600, seed=99):
    '''
    Make a set of n cities, each with random coordinates within a (w x h)
    rectangle.'''
    random.seed(seed * n)
    return frozenset(City(random.randrange(width), random.randrange(height)) \
                     for c in range(n))


route = alltours_tsp(Cities(9))
dis = tour_length(route)

print(route)
print(dis)

def plot_tour(tour):
    '''
    Plot the cities as circles and the tour as lines between them.'''
    plot_lines(list(tour) + [tour[0]])
    plt.show()

def plot_lines(points, style='bo-'):
    '''
    Plot lines to connect a series of points.'''
    
    plt.plot(list(map(X, points)), list(map(Y, points)), style)
    plt.axis('scaled');plt.axis('off')
    

plot_tour(route)

def plot_tsp(algorithm, cities):
    pass
    



