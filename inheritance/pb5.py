class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"    
    
 

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(6, 7)

print(v1 + v2)  # Vector(6, 8)
print(v1 * 2)   # Vector(4, 6)

print(v1 + v3)  # Vector(8, 10)
print(v1 - v3)  # Vector(-4, -4)