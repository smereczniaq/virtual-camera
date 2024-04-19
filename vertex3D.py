import numpy as np

class Vertex3D:
    def __init__(self, x, y, z):
        self.start_x = x
        self.start_y = y
        self.start_z = z
        
        self.x = x
        self.y = y
        self.z = z

    def coordinates_matrix(self):
        return np.array([
            [self.x],
            [self.y], 
            [self.z], 
            [1]
            ])

    def operate(self, matrix):
        coordinates_matrix = self.coordinates_matrix()

        new_coordinates = np.dot(matrix, coordinates_matrix)
        new_coordinates = new_coordinates.flatten()

        self.x = new_coordinates[0]
        self.y = new_coordinates[1]
        self.z = new_coordinates[2]
