import pygame
from vertex2D import Vertex2D
import random
import numpy as np

class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

class Polygon:
    def __init__(self, vertices, edges, color):
        self.vertices = vertices
        self.edges = edges
        self.color = color

    def center_of_mass(self):
        x = sum([vertex.x for vertex in self.vertices]) / len(self.vertices)
        y = sum([vertex.y for vertex in self.vertices]) / len(self.vertices)
        z = sum([vertex.z for vertex in self.vertices]) / len(self.vertices)
        
        return x, y, z

    
    def plane(self):
        vertex1 = self.vertices[0]
        vertex2 = self.vertices[1]
        vertex3 = self.vertices[2]

        a1 = vertex2.x - vertex1.x
        b1 = vertex2.y - vertex1.y
        c1 = vertex2.z - vertex1.z

        a2 = vertex3.x - vertex1.x
        b2 = vertex3.y - vertex1.y
        c2 = vertex3.z - vertex1.z

        A = b1 * c2 - b2 * c1
        B = a2 * c1 - a1 * c2
        C = a1 * b2 - b1 * a2
        D = (-A * vertex1.x - B * vertex1.y - C * vertex1.z)

        return A, B, C, D


    def draw(self, screen, width, height, d):
        move_x = width / 2
        move_y = height / 2
        polygon_color = self.color

        points = []
        edges = []
        edge_color = (0, 0, 0)
        for edge in self.edges:
            vertex1 = edge.vertex1
            vertex2 = edge.vertex2

            vertex1_2d = Vertex2D(vertex1.x, vertex1.y, vertex1.z, d)
            vertex2_2d = Vertex2D(vertex2.x, vertex2.y, vertex2.z, d)

            x1 = vertex1_2d.x + move_x
            y1 = vertex1_2d.y + move_y
            x2 = vertex2_2d.x + move_x
            y2 = vertex2_2d.y + move_y

            points.append((x1, y1))
            edges.append([(x1, y1), (x2, y2)])

        if len(points) > 2:
            pygame.draw.polygon(screen, polygon_color, points, 0)

        for edge in edges:
            pygame.draw.line(screen, edge_color, edge[0], edge[1], 1)

            
            