class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        """Overload the str() function to print the vector in a readable format."""
        return f"Vector({self.x}, {self.y})"


# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
v4 = v1 - v2

print(v3)  # Output: Vector(6, 8)
print(v4)  # Output: Vector(-2, -2)
