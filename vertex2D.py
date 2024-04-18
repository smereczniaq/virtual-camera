class Vertex2D:
    def __init__(self, x, y, z, d):
        self.x = (x * d) / z
        self.y = (y * d) / z


    