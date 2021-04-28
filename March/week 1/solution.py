class Point:
    def __init__(self, p_x, p_y, p_z):
        self.p_x = p_x
        self.p_y = p_y
        self.p_z = p_z

    def __str__(self):
        print(f'Point(x={self.p_x}, y={self.p_y}, z={self.p_z})')


p1 = Point(1, 2, 3)
