import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector2D<' + str(self.x) + ',' + str(self.y) + '>'

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def multiply(self, other):
        if type(other) == Vector2D:
            return self.x * other.x + self.y * other.y
        else:
            return Vector2D(self.x * other, self.y * other)

    def divide(self, other):
        return Vector2D(self.x / other, self.y / other)

    def magnitude(self):
        return math.sqrt(self.multiply(self))

    def angle(self):
        return math.atan(self.y / self.x)

    def project_onto(self, v):
        return v.multiply(self.multiply(v) / v.magnitude()**2)

class TopoVector2D(Vector2D):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
