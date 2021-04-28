import math


class Circle:
    """
    Class Circle
    """

    def __init__(self, radius=1.0):
        """
        Circle radius initialization
        """
        self.radius = radius

    @property  # this acts as the getter
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("radius cannot be negative")
        self.__radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def __str__(self):
        return f"Circle({self.radius})"

    def __repr__(self):
        return f"Circle({self.radius})"



