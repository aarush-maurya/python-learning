import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius**2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def sector_area(self, radian=None, length=None):
        if radian is not None:
            return (1 / 2) * (self.radius**2) * radian
        elif length is not None:
            return self.radius * length
        else:
            raise ValueError("Expected only one argument, either radian or length")
