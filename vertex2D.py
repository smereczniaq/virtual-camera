class Vertex2D:
    def __init__(self, x, y, z, d):
        z = self.normalize_z(z)

        self.x = (x * d) / z
        self.y = (y * d) / z

    def normalize_z(self, z):
        if z < 1:
            z = 1

        return z


    