import pygame
from vertex2D import Vertex2D
import numpy as np
from polygon import Polygon, Edge
import networkx as nx
from itertools import combinations

class Figure():
    def __init__(self, polygons):
        self.polygons = polygons

    def move(self, matrix):
        for polygon in self.polygons:
            for vertex in polygon.vertices:
                vertex.operate(matrix)

    def rotate(self, matrix):
        for polygon in self.polygons:
            for vertex in polygon.vertices:
                vertex.operate(matrix)
    
