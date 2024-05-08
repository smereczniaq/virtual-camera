from figure import Figure
from vertex3D import Vertex3D
from vertex2D import Vertex2D
from polygon import Edge, Polygon
import json
import numpy as np
import random
from bsp_tree import build_bsp_tree, traverse_bsp_tree

translation_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

class Scene:
    def __init__(self, file_name):
        self.file_name = file_name
        self.figures = self.load_figures(file_name)

    def load_figures(self, file_name):
        figures = list()
        with open(file_name) as f:
            data = f.read()
            lines = data.strip().split("\n")

        for line in lines:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            vertices_part, edges_part, polygons_part = line.split(";")
            vertices_str = vertices_part.split("|")
            edges_str = edges_part.split("|")
            polygons_str = polygons_part.split("|")

            vertices = [vertex_str.split(",") for vertex_str in vertices_str]
            edges = [edge_str.split(",") for edge_str in edges_str]
            polygons = [polygon_str.split(",") for polygon_str in polygons_str]

            vertices_float = [[float(coord) for coord in vertex] for vertex in vertices]
            edges_int = [[int(coord) for coord in edge] for edge in edges]
            polygons_int = [[int(coord) for coord in polygon] for polygon in polygons]

            vertices3d = [Vertex3D(vertex[0], vertex[1], vertex[2]) for vertex in vertices_float]
            edges3d = [Edge(vertices3d[edge[0]], vertices3d[edge[1]]) for edge in edges_int]
            polygons3d = list()
            for polygon in polygons_int:
                edges = [edges3d[edge] for edge in polygon]
                vertices1 = [edge.vertex1 for edge in edges]
                vertices2 = [edge.vertex2 for edge in edges]
                vertices = list(set(vertices1 + vertices2))
                polygons3d.append(Polygon(vertices, edges, color))

            figures.append(Figure(polygons3d))

        return figures

    def load_polygons(self):
        polygons = list()
        for fig in self.figures:
            for polygon in fig.polygons:
                polygons.append(polygon)

        return polygons

    def move(self, vector):
        move_matrix = translation_matrix.copy()
        move_matrix[0:3, -1] += vector

        for fig in self.figures:
            fig.move(move_matrix)

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

        for fig in self.figures:
            fig.rotate(rotation_matrix)


    def reload(self):
        return Scene(self.file_name)


    def draw(self, screen, width, height, d):
        polygons = self.load_polygons()
        bsp_tree = build_bsp_tree(polygons)
        sorted_polygons = traverse_bsp_tree(bsp_tree)
        for polygon in sorted_polygons:
            polygon.draw(screen, width, height, d)
