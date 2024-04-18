import pygame
from vertex2D import Vertex2D

class Cube:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def draw(self, screen, width, height, d):
        move_x = width / 2
        move_y = height / 2

        for edge in self.edges:
            vertex1 = edge.vertex1
            vertex2 = edge.vertex2

            vertex1_2d = Vertex2D(vertex1.x, vertex1.y, vertex1.z, d)
            vertex2_2d = Vertex2D(vertex2.x, vertex2.y, vertex2.z, d)

            x1 = vertex1_2d.x + move_x
            y1 = vertex1_2d.y + move_y
            x2 = vertex2_2d.x + move_x
            y2 = vertex2_2d.y + move_y

            pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2))

    def move(self, matrix):
        for vertex in self.vertices:
            vertex.operate(matrix)

    def rotate(self, matrix):
        for vertex in self.vertices:
            vertex.operate(matrix)
