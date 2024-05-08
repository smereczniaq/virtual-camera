import numpy as np
import random

class BSPNode:
    def __init__(self, polygons):
        self.polygons = polygons
        self.front = None
        self.back = None
        self.partition_plane_polygon = None

def build_bsp_tree(polygons):
    if not polygons:
        return None
    
    node = BSPNode(polygons)
    start_index = 0
    node.partition_plane_polygon = polygons[start_index]

    front_polygons = list()
    back_polygons = list()

    for idx, polygon in enumerate(polygons):
        if idx == start_index or polygon.center_of_mass()[2] < 0:
            continue

        side = classify_polygon(polygon, node.partition_plane_polygon.plane())
        if side == 1:
            front_polygons.append(polygon)
        elif side == -1:
            back_polygons.append(polygon)
        else:
            front_polygons.append(polygon)
            back_polygons.append(polygon)

    node.front = build_bsp_tree(front_polygons)
    node.back = build_bsp_tree(back_polygons)
    return node


def classify_polygon(polygon, plane):
    center_of_mass = polygon.center_of_mass()
    return classify_point(center_of_mass, plane)

def classify_point(point, plane):
    A, B, C, D = plane
    x, y, z = point[0], point[1], point[2]
    distance = A * x + B * y + C * z + D
    if distance > 0:
        return 1
    elif distance < 0:
        return -1
    else:
        return 0


def traverse_bsp_tree(node):
    point = (0, 0, 0)
    if node is None:
        return list()
    result = classify_point(point, node.partition_plane_polygon.plane())
    if result == 1:
        return traverse_bsp_tree(node.back) + [node.partition_plane_polygon] +traverse_bsp_tree(node.front)
    elif result == -1:
        return traverse_bsp_tree(node.front)+ [node.partition_plane_polygon] + traverse_bsp_tree(node.back) 
    else:
        return traverse_bsp_tree(node.front) + traverse_bsp_tree(node.back) 