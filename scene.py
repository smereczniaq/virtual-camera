from cube import Cube
from vertex3D import Vertex3D
from vertex2D import Vertex2D
from edge import Edge
import json
import numpy as np

translation_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

class Scene:
    def __init__(self, file_name):
        self.file_name = file_name
        self.objects = self.load_objects(file_name)

    def load_objects(self, file_name):
        objects = list()
        with open(file_name) as f:
            data = f.read()
            lines = data.strip().split("\n")

        for line in lines:
            vertices_part, edges_part = line.split(";")
            vertices_str = vertices_part.split("|")
            edges_str = edges_part.split("|")

            vertices = [vertex_str.split(",") for vertex_str in vertices_str]
            edges = [edge_str.split(",") for edge_str in edges_str]

            vertices_float = [[float(coord) for coord in vertex] for vertex in vertices]
            edges_int = [[int(coord) for coord in edge] for edge in edges]

            vertices3d = [Vertex3D(vertex[0], vertex[1], vertex[2]) for vertex in vertices_float]
            edges3d = [Edge(vertices3d[edge[0]], vertices3d[edge[1]]) for edge in edges_int]

            objects.append(Cube(vertices3d, edges3d))

        return objects

    def move(self, vector):
        move_matrix = translation_matrix.copy()
        move_matrix[0:3, -1] += vector

        for obj in self.objects:
            obj.move(move_matrix)

    def rotate(self, axis, angle):
        angle = np.radians(angle)
        if axis == "x":
            rotation_matrix = np.array([
                [1, 0, 0, 0],
                [0, np.cos(angle), -np.sin(angle), 0],
                [0, np.sin(angle), np.cos(angle), 0],
                [0, 0, 0, 1]
            ])
        elif axis == "y":
            rotation_matrix = np.array([
                [np.cos(angle), 0, np.sin(angle), 0],
                [0, 1, 0, 0],
                [-np.sin(angle), 0, np.cos(angle), 0],
                [0, 0, 0, 1]
            ])
        elif axis == "z":
            rotation_matrix = np.array([
                [np.cos(angle), -np.sin(angle), 0, 0],
                [np.sin(angle), np.cos(angle), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        for obj in self.objects:
            obj.rotate(rotation_matrix)


    def reload(self):
        return Scene(self.file_name)
