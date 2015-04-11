#! needed libraries 
from __future__ import division
import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv


file_xy = open(r'J:\四会多规合一\四会景点坐标.csv')


def all_points_plot(file):
    reader_all = csv.reader(file, delimiter=',', skipinitialspace=True)
    x_all = []
    y_all = []
    for row in reader_all:
        if row[0] != '':
            y_all.append(float(row[1]))# latitude as Y coordinate
            x_all.append(float(row[2]))# longitude as X coordinate
    return (x_all, y_all)


test = all_points_plot(file_xy)
print(test)


def func1(x):
    return func2(30) + x

def func2(y):
    return y

test1 = func1(3)
print(test1)
