# Imports
import math
from typing import ValuesView

# Read in the test data

# file = "test_data.txt"
file = "puzzle_data.txt"
course = []
with open(file) as f:
    for line in f:
        course.append(line.strip('\n'))

len(course)
len(course[0])


def calcTree(course, route):
    courseLength = len(course)
    courseWidth = len(course[0])
    horz = route[0] * courseLength
    vert =  courseLength


    multv = math.ceil(horz / courseWidth)
    multv 
    for i in range(0,courseLength):
        course[i] = course[i] * (multv)

    v = range(0,vert,route[1])
    h = range(0,horz,route[0])
    
    trees = []
    for [v, h] in zip(v,h):
        trees.append(course[v][h])

    return trees.count("#")


routes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

treecounts= 1
for route in routes:
    treecounts = treecounts * calcTree(course,route)

treecounts
