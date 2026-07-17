"""
A small dependency-free 2D/3D vector implementation for learning,
small scripts, and lightweight prototypes.

This is not intended to replace NumPy or specialized math libraries.
"""

from typing import Literal
from math import sqrt
from operator import add, sub


class Vector:
    """Vector class for 2D or 3D space."""

    def __init__(self, mode: Literal["2d", "3d"], x, y, z=None):
        self.mode = mode
        self.x = x
        self.y = y
        self.z = z if mode == "3d" else 0
        
    def magnitude(self):
        """
        Calculate the lenght forms by the hypothesis calculation between x and y.
        """
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalized(self):
        """Normalize the vector."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(
            self.mode, 
            self.x / mag, 
            self.y / mag, 
            self.z / mag
            )
        
    def scal_mult(self, scalar: int):
        """Multiply vector by a scalar."""
        return Vector(
            self.mode,
            self.x * scalar, 
            self.y * scalar, 
            self.z * scalar
            )
            
    def __add__(self, other):
        """Add two vectors."""
        return self._lin_combination(other, add)

    def __sub__(self, other):
        """Subtract two vectors."""
        return self._lin_combination(other, sub)

    def _lin_combination(self, other, op):
        """Helper function for vector addition/subtraction."""
        # Promote to the highest dimension involved.
        mode = self.mode if self.mode == other.mode else "3d"
        return Vector(
            mode, 
            op(self.x, other.x), 
            op(self.y, other.y), 
            op(self.z, other.z)
            )
            
    def __repr__(self):
        z = ", " + str(self.z) if self.mode == "3d" else ""
        return f"({self.x}, {self.y}{z})"
        


# Testing
if __name__ == "__main__":
    v1 = Vector("2d", 2, 3)
    v2 = Vector("2d", 0, 4)
    v3 = Vector("3d", 2, 3, 4)
    v4 = Vector("3d", 5, 1, 0)

    assert (v1 + v2).x == 2
    assert (v1 + v2).y == 7
    assert (v3 + v4).z == 4

    assert (v2 - v1).x == -2
    assert (v2 - v1).y == 1

    assert v1.scal_mult(2).x == 4
    assert v3.scal_mult(3).z == 12

    assert abs(v1.magnitude() - sqrt(13)) < 1e-9
    assert abs(v3.magnitude() - sqrt(29)) < 1e-9
    
    print("All tests passed!")
